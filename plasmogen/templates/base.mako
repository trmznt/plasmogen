## -*- coding: utf-8 -*-
% if request and request.is_xhr:
  ${next.body()}

  <script type="text/javascript">
    //<![CDATA[
    ${self.jscode()}
    //]]>
  </script>

% else:

<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8" />
  <title>${request.get_resource('plasmogen.title', None) or "PlasmoGEN"}</title>
  <meta name='viewport' content='width=device-width, initial-scale=1.0' />

  <!-- styles -->
  <link href="${request.static_url('rhombus:static/bootstrap/css/bootstrap.min.css')}" rel="stylesheet" />
  <link href="${request.static_url('rhombus:static/bootstrap/css/bootstrap-theme.min.css')}" rel="stylesheet" />
  <link href="${request.static_url('rhombus:static/fonts/source-sans-pro.css')}" rel="stylesheet" />
  <link href="${request.static_url('rhombus:static/select2/css/select2.min.css')}" rel="stylesheet" />
  <link href="${request.static_url('genaf:static/custom.css')}" rel="stylesheet" />
  ${self.stylelink()}

  </head>
  <body>

    <!-- Static navbar -->
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">${request.get_resource('plasmogen.title', 'PlasmoGEN')}</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <!-- <li class="active"><a href="#">Home</a></li> -->
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Browse <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="/batch">Batch</a></li>
                <li><a href="/location">Location</a></li>
                <li><a href="/sample">Sample</a></li>
                <li role="separator" class="divider"></li>
                <li class="dropdown-header">Microsatellite</li>
                <li><a href="/panel">Panel</a></li>
                <li><a href="/marker">Marker</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Analyze <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">Basic tools</li>
                <li><a href="/tools/allele">Allele summary</a></li>
                <li><a href="/tools/genotype">Genotype summary</a></li>
                <li><a href="/tools/he">Heterozygosity</a></li>
                <li><a href="/tools/moi">Multiplicity of Infection</a></li>
                <li><a href="/tools/pcoa">Principal Coordinate Analysis (PCoA)</a></li>
                <li><a href="/tools/mca">Multiple Correspondence Analysis (MCA)</a></li>
                <li><a href="/tools/nj">Neigbor-Joining (NJ) Tree</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Resources <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="/">Tutorials</a></li>
              </ul>
            </li>


          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a href="./">User: <span class="sr-only">(current)</span></a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
      ${flash_msg()}
      </div>
      <div class="row">

        <div class="col-md-12">
        ${next.body()}
        </div>

      </div>

    </div>
    <footer>
    <div class="container-fluid">
      <div class='row'>
      <div class='col-md-12'>
        <!-- font: Nobile -->
        <p>(C) 2013 - 2015 Menzies School of Health Research, Australia <br />
           (C) 2013 - 2015 Eijkman Institute for Molecular Biology, Indonesia</p>
      </div>
      </div>
    </div>
    </footer>

${self.scriptlinks()}

  </body>

</html>
% endif
##
##
<%def name="stylelink()">
</%def>
##
##
<%def name="scriptlinks()">
    <script src="${request.static_url('rhombus:static/js/jquery.js')}"></script>
    <script src="${request.static_url('rhombus:static/bootstrap/js/bootstrap.min.js')}"></script>
    <script src="${request.static_url('rhombus:static/select2/js/select2.min.js')}"></script>
    <script src="${request.static_url('rhombus:static/js/jquery.ocupload-min.js')}"></script>
    ${self.jslink()}
    <script type="text/javascript">
        //<![CDATA[
        ${self.jscode()}
        //]]>
    </script>
</%def>
##
##
<%def name='flash_msg()'>
% if request.session.peek_flash():

  % for msg_type, msg_text in request.session.pop_flash():
   <div class="alert alert-${msg_type}">
     <a class="close" data-dismiss="alert">×</a>
     ${msg_text}
   </div>
  % endfor

% endif
</%def>

##
<%def name='jscode()'>
</%def>

##
<%def name="jslink()">
</%def>
