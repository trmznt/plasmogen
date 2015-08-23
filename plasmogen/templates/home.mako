<%inherit file="rhombus:templates/base.mako" />

<h1>${request.get_resource('plasmogen.header', "PlasmoGEN - Plasmodium Genotype platform")}</h1>


% if request.user:

<p>You are authenticated as: ${request.user.login}  [<a href="/logout">Logout</a>]</p>

<p>Welcome to ${request.get_resource('plasmogen.title', 'Plasmogen')} What's next?<p>

<ul>
  <li><a href="${request.route_url('genaf.batch-edit', id=0)}">Create a new batch</a>
  <li><a href='${request.route_url("genaf.marker")}'>Check available markers</a></li>
  <li>Browse available panels</li>
  <li><a href='${request.route_url("genaf.batch")}'>Browse available batches</a></li>
</ul>

<p>Available tutorial:</p>
<ul>
  <li>Uploading your data and FSA files (tutorial-01.zip)</li>
  <li>...</li>
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
