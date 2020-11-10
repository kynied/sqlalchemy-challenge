<!DOCTYPE html>
<html lang="en-us"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">

    <title>app.py - Jupyter Text Editor</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon-file.ico?v=e2776a7f45692c839d6eea7d7ff6f3b2">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="app_files/jquery-ui.css" type="text/css">
    <link rel="stylesheet" href="app_files/jquery.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="app_files/codemirror.css">
<link rel="stylesheet" href="app_files/dialog.css">

    <link rel="stylesheet" href="app_files/style.css" type="text/css">
    

    <link rel="stylesheet" href="app_files/custom.css" type="text/css">
    <script src="app_files/promise.js" type="text/javascript" charset="utf-8"></script>
    <script src="app_files/react.js" type="text/javascript"></script>
    <script src="app_files/react-dom.js" type="text/javascript"></script>
    <script src="app_files/index.js" type="text/javascript"></script>
    <script src="app_files/require.js" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20201109234226",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="app_files/contents.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="app_files/custom.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="codemirror/mode/python/python" src="app_files/python.js"></script></head>

<body class="edit_app" data-base-url="/" data-file-path="untitled.txt" data-jupyter-api-token="ea6b75ad6373b6f74417ae4c28674245db8a2b4041ae9d5c" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=ea6b75ad6373b6f74417ae4c28674245db8a2b4041ae9d5c" title="dashboard">
      <img src="app_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename">app.py</span>
    <div class="dirty-indicator-clean" title="No changes to save"></div><span class="last_modified" title="Tue, Nov 10, 2020 12:02 AM">a minute ago</span>
</span>


  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p class="navbar-text indicator_area">
          <span id="current-mode" title="The current language is Python">Python</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"><div id="notification_save" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="#">New</a></li>
                <li id="save-file"><a href="#">Save</a></li>
                <li id="rename-file"><a href="#">Rename</a></li>
                <li id="download-file"><a href="#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="#">Find</a></li>
                <li id="menu-replace"><a href="#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default" class="selected-keymap"><a href="#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
              <a href="#">Toggle Header</a></li>
              <li id="menu-line-numbers"><a href="#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              <li><a href="#" title="Set language to APL">APL</a></li><li><a href="#" title="Set language to PGP">PGP</a></li><li><a href="#" title="Set language to ASN.1">ASN.1</a></li><li><a href="#" title="Set language to Asterisk">Asterisk</a></li><li><a href="#" title="Set language to Brainfuck">Brainfuck</a></li><li><a href="#" title="Set language to C">C</a></li><li><a href="#" title="Set language to C++">C++</a></li><li><a href="#" title="Set language to Cobol">Cobol</a></li><li><a href="#" title="Set language to C#">C#</a></li><li><a href="#" title="Set language to Clojure">Clojure</a></li><li><a href="#" title="Set language to ClojureScript">ClojureScript</a></li><li><a href="#" title="Set language to Closure Stylesheets (GSS)">Closure Stylesheets (GSS)</a></li><li><a href="#" title="Set language to CMake">CMake</a></li><li><a href="#" title="Set language to CoffeeScript">CoffeeScript</a></li><li><a href="#" title="Set language to Common Lisp">Common Lisp</a></li><li><a href="#" title="Set language to Cypher">Cypher</a></li><li><a href="#" title="Set language to Cython">Cython</a></li><li><a href="#" title="Set language to Crystal">Crystal</a></li><li><a href="#" title="Set language to CSS">CSS</a></li><li><a href="#" title="Set language to CQL">CQL</a></li><li><a href="#" title="Set language to D">D</a></li><li><a href="#" title="Set language to Dart">Dart</a></li><li><a href="#" title="Set language to diff">diff</a></li><li><a href="#" title="Set language to Django">Django</a></li><li><a href="#" title="Set language to Dockerfile">Dockerfile</a></li><li><a href="#" title="Set language to DTD">DTD</a></li><li><a href="#" title="Set language to Dylan">Dylan</a></li><li><a href="#" title="Set language to EBNF">EBNF</a></li><li><a href="#" title="Set language to ECL">ECL</a></li><li><a href="#" title="Set language to edn">edn</a></li><li><a href="#" title="Set language to Eiffel">Eiffel</a></li><li><a href="#" title="Set language to Elm">Elm</a></li><li><a href="#" title="Set language to Embedded Javascript">Embedded Javascript</a></li><li><a href="#" title="Set language to Embedded Ruby">Embedded Ruby</a></li><li><a href="#" title="Set language to Erlang">Erlang</a></li><li><a href="#" title="Set language to Esper">Esper</a></li><li><a href="#" title="Set language to Factor">Factor</a></li><li><a href="#" title="Set language to FCL">FCL</a></li><li><a href="#" title="Set language to Forth">Forth</a></li><li><a href="#" title="Set language to Fortran">Fortran</a></li><li><a href="#" title="Set language to F#">F#</a></li><li><a href="#" title="Set language to Gas">Gas</a></li><li><a href="#" title="Set language to Gherkin">Gherkin</a></li><li><a href="#" title="Set language to GitHub Flavored Markdown">GitHub Flavored Markdown</a></li><li><a href="#" title="Set language to Go">Go</a></li><li><a href="#" title="Set language to Groovy">Groovy</a></li><li><a href="#" title="Set language to HAML">HAML</a></li><li><a href="#" title="Set language to Haskell">Haskell</a></li><li><a href="#" title="Set language to Haskell (Literate)">Haskell (Literate)</a></li><li><a href="#" title="Set language to Haxe">Haxe</a></li><li><a href="#" title="Set language to HXML">HXML</a></li><li><a href="#" title="Set language to ASP.NET">ASP.NET</a></li><li><a href="#" title="Set language to HTML">HTML</a></li><li><a href="#" title="Set language to HTTP">HTTP</a></li><li><a href="#" title="Set language to IDL">IDL</a></li><li><a href="#" title="Set language to Pug">Pug</a></li><li><a href="#" title="Set language to Java">Java</a></li><li><a href="#" title="Set language to Java Server Pages">Java Server Pages</a></li><li><a href="#" title="Set language to JavaScript">JavaScript</a></li><li><a href="#" title="Set language to JSON">JSON</a></li><li><a href="#" title="Set language to JSON-LD">JSON-LD</a></li><li><a href="#" title="Set language to JSX">JSX</a></li><li><a href="#" title="Set language to Jinja2">Jinja2</a></li><li><a href="#" title="Set language to Julia">Julia</a></li><li><a href="#" title="Set language to Kotlin">Kotlin</a></li><li><a href="#" title="Set language to LESS">LESS</a></li><li><a href="#" title="Set language to LiveScript">LiveScript</a></li><li><a href="#" title="Set language to Lua">Lua</a></li><li><a href="#" title="Set language to Markdown">Markdown</a></li><li><a href="#" title="Set language to mIRC">mIRC</a></li><li><a href="#" title="Set language to MariaDB SQL">MariaDB SQL</a></li><li><a href="#" title="Set language to Mathematica">Mathematica</a></li><li><a href="#" title="Set language to Modelica">Modelica</a></li><li><a href="#" title="Set language to MUMPS">MUMPS</a></li><li><a href="#" title="Set language to MS SQL">MS SQL</a></li><li><a href="#" title="Set language to mbox">mbox</a></li><li><a href="#" title="Set language to MySQL">MySQL</a></li><li><a href="#" title="Set language to Nginx">Nginx</a></li><li><a href="#" title="Set language to NSIS">NSIS</a></li><li><a href="#" title="Set language to NTriples">NTriples</a></li><li><a href="#" title="Set language to Objective-C">Objective-C</a></li><li><a href="#" title="Set language to OCaml">OCaml</a></li><li><a href="#" title="Set language to Octave">Octave</a></li><li><a href="#" title="Set language to Oz">Oz</a></li><li><a href="#" title="Set language to Pascal">Pascal</a></li><li><a href="#" title="Set language to PEG.js">PEG.js</a></li><li><a href="#" title="Set language to Perl">Perl</a></li><li><a href="#" title="Set language to PHP">PHP</a></li><li><a href="#" title="Set language to Pig">Pig</a></li><li><a href="#" title="Set language to Plain Text">Plain Text</a></li><li><a href="#" title="Set language to PLSQL">PLSQL</a></li><li><a href="#" title="Set language to PostgreSQL">PostgreSQL</a></li><li><a href="#" title="Set language to PowerShell">PowerShell</a></li><li><a href="#" title="Set language to Properties files">Properties files</a></li><li><a href="#" title="Set language to ProtoBuf">ProtoBuf</a></li><li><a href="#" title="Set language to Python">Python</a></li><li><a href="#" title="Set language to Puppet">Puppet</a></li><li><a href="#" title="Set language to Q">Q</a></li><li><a href="#" title="Set language to R">R</a></li><li><a href="#" title="Set language to reStructuredText">reStructuredText</a></li><li><a href="#" title="Set language to RPM Changes">RPM Changes</a></li><li><a href="#" title="Set language to RPM Spec">RPM Spec</a></li><li><a href="#" title="Set language to Ruby">Ruby</a></li><li><a href="#" title="Set language to Rust">Rust</a></li><li><a href="#" title="Set language to SAS">SAS</a></li><li><a href="#" title="Set language to Sass">Sass</a></li><li><a href="#" title="Set language to Scala">Scala</a></li><li><a href="#" title="Set language to Scheme">Scheme</a></li><li><a href="#" title="Set language to SCSS">SCSS</a></li><li><a href="#" title="Set language to Shell">Shell</a></li><li><a href="#" title="Set language to Sieve">Sieve</a></li><li><a href="#" title="Set language to Slim">Slim</a></li><li><a href="#" title="Set language to Smalltalk">Smalltalk</a></li><li><a href="#" title="Set language to Smarty">Smarty</a></li><li><a href="#" title="Set language to Solr">Solr</a></li><li><a href="#" title="Set language to SML">SML</a></li><li><a href="#" title="Set language to Soy">Soy</a></li><li><a href="#" title="Set language to SPARQL">SPARQL</a></li><li><a href="#" title="Set language to Spreadsheet">Spreadsheet</a></li><li><a href="#" title="Set language to SQL">SQL</a></li><li><a href="#" title="Set language to SQLite">SQLite</a></li><li><a href="#" title="Set language to Squirrel">Squirrel</a></li><li><a href="#" title="Set language to Stylus">Stylus</a></li><li><a href="#" title="Set language to Swift">Swift</a></li><li><a href="#" title="Set language to sTeX">sTeX</a></li><li><a href="#" title="Set language to LaTeX">LaTeX</a></li><li><a href="#" title="Set language to SystemVerilog">SystemVerilog</a></li><li><a href="#" title="Set language to Tcl">Tcl</a></li><li><a href="#" title="Set language to Textile">Textile</a></li><li><a href="#" title="Set language to TiddlyWiki ">TiddlyWiki </a></li><li><a href="#" title="Set language to Tiki wiki">Tiki wiki</a></li><li><a href="#" title="Set language to TOML">TOML</a></li><li><a href="#" title="Set language to Tornado">Tornado</a></li><li><a href="#" title="Set language to troff">troff</a></li><li><a href="#" title="Set language to TTCN">TTCN</a></li><li><a href="#" title="Set language to TTCN_CFG">TTCN_CFG</a></li><li><a href="#" title="Set language to Turtle">Turtle</a></li><li><a href="#" title="Set language to TypeScript">TypeScript</a></li><li><a href="#" title="Set language to TypeScript-JSX">TypeScript-JSX</a></li><li><a href="#" title="Set language to Twig">Twig</a></li><li><a href="#" title="Set language to Web IDL">Web IDL</a></li><li><a href="#" title="Set language to VB.NET">VB.NET</a></li><li><a href="#" title="Set language to VBScript">VBScript</a></li><li><a href="#" title="Set language to Velocity">Velocity</a></li><li><a href="#" title="Set language to Verilog">Verilog</a></li><li><a href="#" title="Set language to VHDL">VHDL</a></li><li><a href="#" title="Set language to Vue.js Component">Vue.js Component</a></li><li><a href="#" title="Set language to XML">XML</a></li><li><a href="#" title="Set language to XQuery">XQuery</a></li><li><a href="#" title="Set language to Yacas">Yacas</a></li><li><a href="#" title="Set language to YAML">YAML</a></li><li><a href="#" title="Set language to Z80">Z80</a></li><li><a href="#" title="Set language to mscgen">mscgen</a></li><li><a href="#" title="Set language to xu">xu</a></li><li><a href="#" title="Set language to msgenny">msgenny</a></li></ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site" style="display: block; height: 636.433px;">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"><div class="CodeMirror cm-s-ipython CodeMirror-wrap" style="height: 596.433px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 586px; left: 261.4px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1px; height: 1em; outline: currentcolor none medium;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" wrap="off"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="width: 18px; pointer-events: none; display: block; bottom: 0px;"><div style="min-width: 1px; height: 2119px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true" style="height: 18px; pointer-events: none;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 39px; margin-bottom: 0px; border-right-width: 30px; min-height: 2119px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: currentcolor none medium;" role="presentation"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>123</div></div></div><div class="CodeMirror-measure"><pre class="CodeMirror-line" role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">app</span>.<span class="cm-property">run</span>(<span class="cm-variable">debug</span> <span class="cm-operator">=</span> <span class="cm-keyword">False</span>)</span></pre></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-comment">#Importing dependencies</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">flask</span> <span class="cm-keyword">import</span> <span class="cm-variable">Flask</span>, <span class="cm-variable">jsonify</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">import</span> <span class="cm-variable">pandas</span> <span class="cm-keyword">as</span> <span class="cm-variable">pd</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">import</span> <span class="cm-variable">json</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">import</span> <span class="cm-variable">datetime</span> <span class="cm-keyword">as</span> <span class="cm-variable">dt</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">import</span> <span class="cm-variable">sqlalchemy</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">sqlalchemy</span>.<span class="cm-property">ext</span>.<span class="cm-property">automap</span> <span class="cm-keyword">import</span> <span class="cm-variable">automap_base</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">sqlalchemy</span>.<span class="cm-property">orm</span> <span class="cm-keyword">import</span> <span class="cm-variable">Session</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">sqlalchemy</span> <span class="cm-keyword">import</span> <span class="cm-variable">create_engine</span>, <span class="cm-variable">inspect</span>, <span class="cm-variable">func</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-comment">#Setting up the database and getting the tables</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">engine</span> <span class="cm-operator">=</span> <span class="cm-variable">create_engine</span>(<span class="cm-string">"sqlite:///Resources/hawaii.sqlite"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">13</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">14</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">Base</span> <span class="cm-operator">=</span> <span class="cm-variable">automap_base</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">15</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">Base</span>.<span class="cm-property">prepare</span>(<span class="cm-variable">engine</span>, <span class="cm-variable">reflect</span><span class="cm-operator">=</span><span class="cm-keyword">True</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">16</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">17</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">18</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">measurement_table</span> <span class="cm-operator">=</span> <span class="cm-variable">Base</span>.<span class="cm-property">classes</span>.<span class="cm-property">measurement</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">19</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">station_table</span> <span class="cm-operator">=</span> <span class="cm-variable">Base</span>.<span class="cm-property">classes</span>.<span class="cm-property">station</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">20</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">21</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">session</span> <span class="cm-operator">=</span> <span class="cm-variable">Session</span>(<span class="cm-variable">bind</span><span class="cm-operator">=</span><span class="cm-variable">engine</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">22</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">23</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-comment">#Setting up Flask</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">24</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-variable">app</span> <span class="cm-operator">=</span> <span class="cm-variable">Flask</span>(<span class="cm-variable">__name__</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">25</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">26</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-comment">#All the different Flask routes</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">27</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-meta">@app</span>.<span class="cm-property">route</span>(<span class="cm-string">"/"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">28</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">home</span>():</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">29</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> (</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">30</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"Available Routes:&lt;br/&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">31</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"/api/v1.0/precipitation&lt;br&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">32</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"/api/v1.0/stations&lt;br&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">33</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"/api/v1.0/tobs&lt;br&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">34</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"/api/v1.0/&lt;start&gt;&lt;br&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">35</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-string">f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">36</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp;  )</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">37</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">38</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-meta">@app</span>.<span class="cm-property">route</span>(<span class="cm-string">'/api/v1.0/precipitation'</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">39</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">precipitation</span>():</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">40</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">sel</span> <span class="cm-operator">=</span> [<span class="cm-variable">measurement_table</span>.<span class="cm-property">date</span>, <span class="cm-variable">measurement_table</span>.<span class="cm-property">prcp</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">41</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">queryresult</span> <span class="cm-operator">=</span> <span class="cm-variable">session</span>.<span class="cm-property">query</span>(<span class="cm-operator">*</span><span class="cm-variable">sel</span>).<span class="cm-property">all</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">42</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">session</span>.<span class="cm-property">close</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">43</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">44</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">precipitation</span> <span class="cm-operator">=</span> []</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">45</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">for</span> <span class="cm-variable">date</span>, <span class="cm-variable">prcp</span> <span class="cm-keyword">in</span> <span class="cm-variable">queryresult</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">46</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">prcp_dict</span> <span class="cm-operator">=</span> {}</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">47</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">prcp_dict</span>[<span class="cm-string">"Date"</span>] <span class="cm-operator">=</span> <span class="cm-variable">date</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">48</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">prcp_dict</span>[<span class="cm-string">"Precipitation"</span>] <span class="cm-operator">=</span> <span class="cm-variable">prcp</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">49</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">precipitation</span>.<span class="cm-property">append</span>(<span class="cm-variable">prcp_dict</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">50</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">51</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">jsonify</span>(<span class="cm-variable">precipitation</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">52</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">53</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-meta">@app</span>.<span class="cm-property">route</span>(<span class="cm-string">'/api/v1.0/stations'</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">54</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">stations</span>():</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">55</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">sel</span> <span class="cm-operator">=</span> [<span class="cm-variable">station_table</span>.<span class="cm-property">station</span>, <span class="cm-variable">station_table</span>.<span class="cm-property">name</span>, <span class="cm-variable">station_table</span>.<span class="cm-property">latitude</span>, <span class="cm-variable">station_table</span>.<span class="cm-property">longitude</span>, <span class="cm-variable">station_table</span>.<span class="cm-property">elevation</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">56</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">queryresult</span> <span class="cm-operator">=</span> <span class="cm-variable">session</span>.<span class="cm-property">query</span>(<span class="cm-operator">*</span><span class="cm-variable">sel</span>).<span class="cm-property">all</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">57</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">session</span>.<span class="cm-property">close</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">58</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">59</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-variable">stations</span> <span class="cm-operator">=</span> []</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">60</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">for</span> <span class="cm-variable">station</span>, <span class="cm-variable">name</span>, <span class="cm-variable">lat</span>, <span class="cm-variable">lon</span>, <span class="cm-variable">el</span> <span class="cm-keyword">in</span> <span class="cm-variable">queryresult</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">61</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span> <span class="cm-operator">=</span> {}</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">62</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span>[<span class="cm-string">"Station"</span>] <span class="cm-operator">=</span> <span class="cm-variable">station</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">63</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span>[<span class="cm-string">"Name"</span>] <span class="cm-operator">=</span> <span class="cm-variable">name</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">64</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span>[<span class="cm-string">"Lat"</span>] <span class="cm-operator">=</span> <span class="cm-variable">lat</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">65</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span>[<span class="cm-string">"Lon"</span>] <span class="cm-operator">=</span> <span class="cm-variable">lon</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">66</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">station_dict</span>[<span class="cm-string">"Elevation"</span>] <span class="cm-operator">=</span> <span class="cm-variable">el</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">67</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">stations</span>.<span class="cm-property">append</span>(<span class="cm-variable">station_dict</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">68</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">69</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">jsonify</span>(<span class="cm-variable">stations</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">70</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">71</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-meta">@app</span>.<span class="cm-property">route</span>(<span class="cm-string">'/api/v1.0/tobs'</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 26px;">72</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">tobs</span>():</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; border-bottom: 0px solid transparent; top: 2119px;"></div><div class="CodeMirror-gutters" style="height: 2149px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 38px;"></div></div></div></div></div>
</div>


</div>






    


<script src="app_files/main.js" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>