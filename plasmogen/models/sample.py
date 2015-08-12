
from rhombus.models.core import *
from rhombus.models.ek import EK
from rhombus.lib.utils import random_string
from genaf.models.sample import Sample, Batch

from plasmogen.lib import dictfmt

from sqlalchemy import func

# monkey patch / duck punching 

def Batch_add_sample(self, code):
        sample = PlasmogenSample()
        sample.code = code
        sample.batch = self
        return sample

def Batch_search_sample(self, sample_code):
        """ return a single Sample from the current batch with sample_code """
        try:
            return self.samples.filter( 
                func.lower(PlasmogenSample.code) == func.lower(sample_code),
                PlasmogenSample.batch_id == self.id ).one()
        except NoResultFound:
            return None


##Batch.add_sample = Batch_add_sample ## <- this still necessary!!!
##Batch.search_sample = Batch_search_sample
        

@registered
class Subject(BaseMixIn, Base):
    """ subjects """

    __tablename__ = 'subjects'

    code = Column(types.String(24), unique=True, nullable=False)
    yearofbirth = Column(types.Float, nullable=False)
    gender = Column(types.String(1), nullable=False)
    notes = deferred( Column(types.Text()) )


    ## optional fields, unique personal identity
    name = Column(types.String(48))
    birthday = Column(types.Date)
    birthplace = Column(types.String(32))
    idnumber = Column(types.String(32))


    __table_args__ = ( UniqueConstraint( 'code', 'gender', 'yearofbirth' ), {} )

    @staticmethod
    def search( code, gender=None, yearofbirth=None, auto=False, dbsession=None ):
        assert dbsession
        q = Subject.query().filter( and_( Subject.code == code, Subject.gender == gender,
                Subject.yearofbirth == yearofbirth ) )
        r = q.all()
        if len(r) == 0:
            if auto:
                subject = Subject( code = code, gender = gender, yearofbirth = yearofbirth )
                dbsession.add( subject )
                #dbsession.flush()
                return subject
            return None
        return r[0]

    @staticmethod
    def autocode():
        return '#%08x' % random.randrange(256**4)


@registered
class PlasmogenSample(Sample):
    """ PlasmogenSample - Plasmodium Sample

        This class contains information about Plasmodium samples
    """

    passive_case_detection = Column(types.Boolean)

    symptomatic_status = Column(types.Boolean)

    storage_id = Column(types.Integer, ForeignKey('eks.id'), nullable=False)
    storage = EK.proxy('storage_id', '@BLOOD-STORAGE')
    """ sample storage method """

    method_id = Column(types.Integer, ForeignKey('eks.id'), nullable=False)
    method = EK.proxy('method_id', '@BLOOD-WITHDRAWAL')
    """ blood withdrawal method """

    pcr_method_id = Column(types.Integer, ForeignKey('eks.id'), nullable=False)
    pcr_method = EK.proxy('pcr_method_id', '@PCR-METHOD')
    """ PCR method for detection """

    pcr_id = Column(types.Integer, ForeignKey('eks.id'), nullable=False)
    pcr = EK.proxy('pcr_id', '@SPECIES')
    """ species identification based on PCR """

    microscopy_id = Column(types.Integer, ForeignKey('eks.id'), nullable=False)
    microscopy = EK.proxy('microscopy_id', '@SPECIES')
    """ species identification based on microscopy """

    parasitemia = Column(types.Float, nullable=False, default=-1)

    recurrent = Column(types.Boolean, nullable=False, default=False)
    """ if this a recurrent case """

    subject_id = Column(types.Integer, ForeignKey('subjects.id'), nullable=False)
    subject = relationship(Subject, uselist=False,
            backref=backref("samples", lazy='dynamic', passive_deletes=True))
    """ link to subject/individual """

    sampling_order = Column(types.Integer, nullable=False, default = 0)
    """ sampling order for a particular subject/individual """

    __mapper_args__ = { 'polymorphic_identity': 1 }


    def update(self, obj):

        if type(obj) == dict:
            self.storage = obj.get('storage')   # blood storage
            self.method = obj.get('method')     # blood withdrawal method
            self.pcr_method_id = EK._id(obj.get('pcr_method'), grp = '@PCR_METHOD',
                                    dbsession = object_session(self), auto=True)
            self.pcr = obj.get('pcr')
            self.microscopy = obj.get('microscopy')

            # deals with subject
            subject_code = obj.get('subject_code', None)
            related_sample = obj.get('related_sample', None)

            session = object_session(self)

            if subject_code:
                # find subject
                subject = Subject.search(code=subject_code, dbsession = session)
                self.subject_id = subject.id
            elif related_sample:
                # find sample
                sample = Sample.search( code = related_sample, batch_id = self.batch_id )
                self.subject_id = sample.subject_id
            else:
                # create new subject
                while True:
                    code = '#' + random_string(8)
                    # we need to check subject code first !
                    if Subject.query(session).filter(Subject.code == code).count() == 0:
                        break
                subject = Subject( code = code, gender = obj['gender'],
                                    yearofbirth = obj['yearofbirth'] )
                session.add(subject)
                session.flush([subject])
                self.subject = subject

            #self.subject_id = 0

            # now if subject_code & 

        else:

            raise NotImplementedError('PROG/ERR - not implemented yet')

        super().update( obj )        
        return

        if obj.passive_case_detection is not None:
            self.passive_case_detection = obj.passive_case_detection
        if obj.storage_id is not None:
            self.storage_id = 0 #obj.storage_id
        if obj.method_id is not None:
            self.method_id = 0  #obj.method_id
        if obj.pcr_method_id is not None:
            self.pcr_method_id = 0  #obj.pcr_method_id
        if obj.pcr_id is not None:
            self.pcr_id = 0 #obj.pcr_id
        if obj.microscopy_id is not None:
            self.microscopy_id = 0  #obj.microscopy_id
        if obj.recurent is not None:
            self.recurrent = obj.recurrent
        if obj.subject_is:
            self.subject_id = obj.subject_id


    @staticmethod
    def search( subject_id = None, code=None, collection_date=None, location_id=None,
            batch_id = None, auto=False, _q = None ):
        if not _q:
            _q = PlasmoSample.query()
        if code:
            _q = _q.filter( PlasmoSample.code == code )
        if collection_date:
            _q = _q.filter( PlasmoSample.collection_date == collection_date )
        if location_id:
            _q = _q.filter( PlasmoSample.location_id == location_id )
        if batch_id:
            _q = _q.filter( PlasmoSample.batch_id == batch_id )
        #q = q.filter( and_( *filters ) )
        r = _q.all()
        if len(r) == 0:
            if auto:
                if not batch_id:
                    raise RuntimeError('Sample searching with auto-creation must be supplied '
                                        'with batch_id' )
                sample = PlasmoSample( subject_id=subject_id, code=code,
                        location_id=location_id, collection_date=collection_date,
                        batch_id = batch_id)
                #raise RuntimeError(collection_date)
                print('Creating sample with code: %s with batch_id: %d' % 
                        (sample.code, sample.batch_id))
                dbsession.add( sample )
                return sample
            return None
        if len(r) == 1:
            return r[0]
        return r
   

    @staticmethod
    def csv2dict( *args, **kwargs ):
        return dictfmt.csv2dict( *args, **kwargs )
