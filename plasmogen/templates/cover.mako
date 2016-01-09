<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>PlasmoGEN - Plasmodium GENotyping Platform</title>

    <!-- Bootstrap core CSS -->
    <link href="${request.static_url('rhombus:static/bootstrap/css/bootstrap.min.css')}" rel="stylesheet" />

    <!-- Custom styles for this template -->
    <link href="${request.static_url('rhombus:static/cover.css')}" rel="stylesheet">

    <style>
    .intro-section {
    height: 100%;
    padding-top: 150px;
    padding-bottom:150px;
    text-align: center;
}

.features-section {
    height: 100%;
    padding-top: 150px;
    padding-bottom:150px;
    text-align: center;
}

.contact-section {
    height: 100%;
    padding-top: 150px;
    padding-bottom: 150px;
    text-align: center;
}

.spacing-section {
    height: 100%;
    padding-top: 150px;
    padding-bottom: 150px;
    text-align: center;
}
    </style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <h3 class="masthead-brand">PlasmoGEN</h3>
              <nav>
                <ul class="nav masthead-nav">
                  <li><a href="#intro">Home</a></li>
                  <li><a href="#features">Features</a></li>
                  <li><a href="#contact">Contact</a></li>
                </ul>
              </nav>
            </div>
          </div>

        </div>

        <section id="intro" class="intro-section"><div class="cover-container">

          <div class="inner cover">
            <div class='row'>
              <div class='col-md-8'>
                <h1 class="cover-heading">PlasmoGEN<h1>
                <p class="lead">Plasmodium Genotyping Platform</p>
              </div>
              <div class='col-md-4'>
                <form action='/login' method='post'>
                  <fieldset>
                    <input type="text" class="form-control"
                        name='login' placeholder="Login"><br />
                    <input type="password" class="form-control"
                        name='password' placeholder="Password">
                    <input type="hidden" name="came_from" value='/' /><br />
                  </fieldset>
                  <fieldset>
                    <button class="btn btn-primary" type="submit">Login</button>
                  </fieldset>
                </form>
                    <br /><p class="lead">or</p>
                <form action='/login' method='post'>
                  <fieldset>
                    <input type="hidden" name="login" value="guest">
                    <input type="hidden" name="came_from" value="/">
                    <button class="btn btn-primary" type="submit">Login as Guest</button>
                  </fieldset>
                </form>
                <p>By clicking "Login as Guest", you agree to our
                <a>terms of service</a> and
                <a>privacy policy</a>.
                </p>


              </div>
            </div>
            <!--
            <h1 class="cover-heading">Cover your page.</h1>
            <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.</p>
            <p class="lead">
              <a href="#" class="btn btn-lg btn-default">Learn more</a>
            </p>
            -->
          </div>

          <div class="mastfoot">
            <div class="inner">
              <p>(C) 2015 <a href="http://www.menzies.edu.au">Menzies School of Health Research</a> and <a href="http://www.eijkman.go.id">Eijkman Institute for Molecular Biology</a>.</p>
            </div>
          </div>

        </div></section>

        <section id="features" class="features-section"><div class="cover-container">
          <div class="inner-cover">
            <h1 class="cover-heading">Features</h1>
            <div class="row">
              <div class="col-md-12">
                <ul class="lead">
                  <li>Data repository and collaboration</li>
                  <li>Data querying and filtering</li>
                  <li>Integrated DNA microsatellite fragment analysis tool</li>
                  <li>Online comprehensive and explorative analysis</li>
                </ul>
              </div>
            </div>
          </div>

        </div></section>

        <section id="contact" class="contact-section"><div class="cover-container">
          <div class="inner-cover">
            <h1 class="cover-heading">Contact</h1>
            <p class="lead">For general enquiries, please contact <br/> Dr. Sarah Auburn (sarah.auburn [AT] menzies.edu.au)</p>
            <p class="lead">For technical-related enquiries, please contact <br/> Mr. Hidayat Trimarsanto (anto [AT] eijkman.go.id)</p>
          </div>

        </div></section>

        <section id="spacing" class="spacing-section"><div class="cover-container">
          <div class="inner-cover">
            <h1>&nbsp;</h1>
          </div>

        </div></section>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="${request.static_url('rhombus:static/js/jquery.js')}"></script>
    <script src="${request.static_url('rhombus:static/bootstrap/js/bootstrap.min.js')}"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="${request.static_url('rhombus:static/assets/js/ie10-viewport-bug-workaround.js')}"></script>
  </body>
</html>
