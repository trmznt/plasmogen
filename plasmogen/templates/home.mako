<%inherit file="rhombus:templates/base.mako" />
<%!
from rhombus.lib.roles import GUEST
%>

<h1>${request.get_resource('plasmogen.header', "PlasmoGEN - Plasmodium Genotype platform")}</h1>


% if request.user:

<p>You are authenticated as: ${request.user.login}  [<a href="/logout">Logout</a>]</p>

<p>Welcome to ${request.get_resource('plasmogen.title', 'Plasmogen')} What's next?<p>

<div class="row">
  <div class="col-sm-4 col-md-2">
  <a href='${request.route_url("genaf.batch")}' class="btn btn-primary btn-block"
  style="white-space: normal;">
  % if not request.user.has_roles(GUEST):
  <h4><b>Manage data</b></h4>
  <p>Manage your batches, samples and molecular data</p>
  <span class="fa fa-upload fa-5x"></span><br/>&nbsp;</a>
  % else:
  <h4><b>Browse data</b></h4>
  <p>Browse public batches, samples and molecular data</p>
  <span class="fa fa-upload fa-5x"></span><br/>&nbsp;</a>
  % endif
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

% if 'plasmogen.demo.url' in request.registry.settings:

<p>For full tutorial which include data uploading and data cleaning sessions, please go to the demo site by following this
<a href="${request.registry.settings['plasmogen.demo.url']}">link</a>.</p>

<p>Tutorial for this site:</p>
<ul>
  <li><a href="/docs/tutorials/03/index.rst">Data analysis</a></li>
  <li><a href="/docs/tutorials/04/index.rst">Data analysis with custom query</a></li>
  <li><a href="/docs/tutorials/05/index.rst">Data analysis with YAML query</a></li>
</ul>

% else:

<p>Available tutorial:</p>
<ul>
  <li>Tutorial 1 - <a href="/docs/tutorials/01/index.rst">Uploading your data</a></li>
  <li>Tutorial 2 - <a href="/docs/tutorials/02/index.rst">Inspecting FSA files and data cleaning</a></li>
  <li>Tutorial 3 - <a href="/docs/tutorials/03/index.rst">Data analysis</a></li>
  <li>Tutorial 4 - <a href="/docs/tutorials/04/index.rst">Data analysis with custom query</a></li>
  <li>Tutorial 5 - <a href="/docs/tutorials/05/index.rst">Data analysis with YAML query</a></li>
</ul>

% endif

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
