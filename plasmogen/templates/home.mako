<%inherit file="rhombus:templates/base.mako" />

<h1>PlasmoGEN - Plasmodium Genotype platform</h1>


% if request.user:

<p>You are authenticated as: ${request.user.login}  [<a href="/logout">Logout</a>]</p>

<ul>
  <li><a href='${request.route_url("genaf.marker")}'>Markers</a></li>
  <li>Panels</li>
  <li><a href='${request.route_url("genaf.batch")}'>Batches</a></li>
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
