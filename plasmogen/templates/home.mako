<%inherit file="rhombus:templates/base.mako" />

<h1>${request.get_resource('plasmogen.header', "PlasmoGEN - Plasmodium Genotype platform")}</h1>


% if request.user:

<p>You are authenticated as: ${request.user.login}  [<a href="/logout">Logout</a>]</p>

<p>Welcome to ${request.get_resource('plasmogen.title', 'Plasmogen')} What's next?<p>

<div class="row">
  <div class="col-sm-4 col-md-2">
  <a href='${request.route_url("genaf.batch")}' class="btn btn-primary btn-block"
  style="white-space: normal;">
  <h4><b>Manage data</b></h4>
  <p>Manage your batches, samples and molecular data</p>
  <span class="fa fa-upload fa-5x"></span><br/>&nbsp;</a>
  </div>
  <div class="col-sm-4 col-md-2">
  <a href='${request.route_url("genaf.marker")}' class="btn btn-primary btn-block"
  style="white-space: normal;">
  <h4><b>Browse markers</b></h4>
  <p>See available microsatellite markers</p>
  <span class="fa fa-map-marker fa-5x"></span><br />&nbsp;</a>
  </div>
  <div class="col-sm-4 col-md-2">
  <a href='${request.route_url("genaf.panel")}' class="btn btn-primary btn-block"
  style="white-space: normal;">
  <h4><b>Browse panels</b></h4>
  <p>See available microsatellite panel combinations</p>
  <span class="fa fa-map-marker fa-5x"></span><br />&nbsp;</a>
  </div>
  <div class="col-sm-4 col-md-2">
  <a href='${request.route_url("genaf.marker")}' class="btn btn-primary btn-block"
  style="white-space: normal;">
  <h4><b>Analyze data</b></h4>
  <p>Perform data filtering and exploratory data analysis</p>
  <span class="fa fa-bar-chart fa-5x"></span><br />&nbsp;</a>
  </div>
  <div class="col-sm-4 col-md-2">
  <a href='/docs/index.rst' class="btn btn-primary btn-block"
  style="white-space: normal;">
  <h4><b>Browse manuals</b></h4>
  <p>Browse available user guides and tutorials</p>
  <span class="fa fa-book fa-5x"></span><br />&nbsp;</a>
  </div>


</div>

<br />&nbsp;<br />

<p>Available tutorial:</p>
<ul>
  <li>Uploading your data and FSA files (<a href="https://www.dropbox.com/s/75qfjg29gdc0kdj/tutorial_01.zip?dl=0">tutorial-01.zip</a>)</li>
  <li>Adding individual sample and FSA files (tutorial-02.zip)</li>
  <li>Processing and assessing assay (FSA) files (tutorial-03.zip)</li>
  <li>Performing simple, general analysis on your data (tutorial-04.zip)</li>
</ul>

% else:

<div class="login-form">
  <h2>Login</h2>
  <form action="/login" method="post">
    <fieldset>
      <div class="clearfix">
        <label>Username</label>
        <input type="text" name='login' class='span2' />
      </div>
      <div class="clearfix">
        <label>Password</label>
        <input type="password" name='password' class='span2' />
      </div>
      <input type="hidden" name="came_from" value='/' />
      <button class="btn btn-primary" type="submit">Sign in</button>
    </fieldset>
  </form>
</div>

% endif
