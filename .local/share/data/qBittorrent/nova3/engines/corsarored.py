
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1,width=device-width">
  <meta name="selected-link" value="repo_source">

  
<meta name="octolytics-dimension-device" content="mobile" />
<meta name="octolytics-dimension-user_id" content="3889083" /><meta name="octolytics-dimension-user_login" content="dandag" /><meta name="octolytics-dimension-repository_id" content="171283554" /><meta name="octolytics-dimension-repository_nwo" content="dandag/qBittorrent_search_engine" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="171283554" /><meta name="octolytics-dimension-repository_network_root_nwo" content="dandag/qBittorrent_search_engine" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="DF62:7423:104C86F:1CD5238:5CB294AF" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="12778154" /><meta name="octolytics-actor-login" content="Arthoruis" /><meta name="octolytics-actor-hash" content="90649b2e30774a799fe1954c550389749fa4f78394ad3a70c14f6b5d2b13aff4" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="644509ee0099d1c55df305b1b420ac25">

<meta class="js-ga-set" name="dimension1" content="Logged In">

  <meta class="js-ga-set" name="dimension3" content="mobile">


  

  <title>qBittorrent_search_engine/corsarored.py at master · dandag/qBittorrent_search_engine</title>

  <link crossorigin="anonymous" media="all" integrity="sha512-PNrWYcSQNTCjRTlqcI0ZQU4IPe9ep6L46+oSch7UXTgx0v336SCP+9M1JBUw4tMdm8IZAd2MAdREqBA3/29aPA==" rel="stylesheet" href="https://github.githubassets.com/assets/mobile-8e8e5b12902d5f04bad25bdd1b689f64.css" />


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">

  <link rel="apple-touch-icon" href="https://github.githubassets.com/apple-touch-icon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="https://github.githubassets.com/apple-touch-icon-180x180.png">
  <meta name="apple-mobile-web-app-title" content="GitHub">



  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="page-responsive">
    


  <header class="Header-old f5 lh-default clearfix">
    <div class="p-responsive flex-justify-between">
        <div class="d-flex flex-justify-between flex-items-center position-absolute right-0 left-0 px-3 mt-1">
          <div class="d-flex mx-2"><!-- placeholder for hamburger --></div>
          <div class="px-3 overflow-hidden">
                <div class="css-truncate css-truncate-target width-fit">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <strong>
      <a class="text-white" href="/dandag">dandag</a>
    </strong> /
    <strong>
      <a class="text-white" href="/dandag/qBittorrent_search_engine">qBittorrent_search_engine</a>
    </strong>
  </div>

          </div>

          <div class="d-flex flex-items-center">
            
              <a class="position-relative notification-indicator ml-3" href="/notifications"
                    aria-label="You have unread notifications"
                  data-ga-click="Mobile, tap, location:header; text:Notifications">
                <span class="mail-status unread"></span>
                <svg height="16" class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
              </a>
          </div>
        </div>


        <details class="details-reset">
          <summary class="mt-1 float-left position-relative user-select-none" data-ga-click="Mobile, tap, location:header; text:Hamburger">
            <svg height="24" class="octicon octicon-three-bars notification-indicator" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </summary>
              <div style="clear: both;">
        <div class="py-3">
          <div class="header-search mr-3 scoped-search site-scoped-search js-site-search position-relative "
  role="search"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="171283554" data-scoped-search-url="/dandag/qBittorrent_search_engine/search" data-unscoped-search-url="/search" action="/dandag/qBittorrent_search_engine/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0  js-chromeless-input-container">
            <a class="header-search-scope no-underline" href="/dandag/qBittorrent_search_engine/blob/master/corsarored.py">This repository</a>
        <input type="text"
          class="form-control input-sm header-search-input  js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-label="Search this repository"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
      </label>
</form>  </div>
</div>

        </div>
      <ul class="text-bold list-style-none p-0 m-0">
            <li>
              <a href="/" data-ga-click="Mobile, tap, location:header; text:Dashboard" class="js-selected-navigation-item HeaderNavlink py-2 mt-3">
                Dashboard
              </a>
            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/issues">
                Issues
</a>            </li>
              <li>
                <a class="js-selected-navigation-item HeaderNavlink py-2" data-ga-click="Mobile, tap, location:header; text:Marketplace" href="/marketplace">
                  Marketplace
</a>              </li>
          <li>
            <a href="/explore" data-ga-click="Mobile, tap, location:header; text:Explore" class="js-selected-navigation-item HeaderNavlink py-2">
              Explore
            </a>
          </li>
            <li>
              <a href="/Arthoruis" data-ga-click="Mobile, tap, location:header; text:User avatar" class="js-selected-navigation-item HeaderNavlink py-2">
                <img class="avatar" src="https://avatars1.githubusercontent.com/u/12778154?s=40&amp;v=4" width="20" height="20" alt="@Arthoruis" />
                Arthoruis
              </a>
            </li>
            <li>
              <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out" class="HeaderNavlink py-2" style="padding-left: 2px;">
                <svg style="margin-right: 2px;" class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"/></svg>
                Sign out
              </a>
            </li>
      </ul>
    </div>

        </details>
    </div>
  </header>

    



    




<div class="reponav-wrapper lh-default">
  <nav class="reponav js-reponav"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /dandag/qBittorrent_search_engine" href="/dandag/qBittorrent_search_engine">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /dandag/qBittorrent_search_engine/issues" href="/dandag/qBittorrent_search_engine/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /dandag/qBittorrent_search_engine/pulls" href="/dandag/qBittorrent_search_engine/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /dandag/qBittorrent_search_engine/projects" href="/dandag/qBittorrent_search_engine/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /dandag/qBittorrent_search_engine/wiki" href="/dandag/qBittorrent_search_engine/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /dandag/qBittorrent_search_engine/pulse" href="/dandag/qBittorrent_search_engine/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a class="js-selected-navigation-item reponav-item" data-selected-links="community /dandag/qBittorrent_search_engine/community" href="/dandag/qBittorrent_search_engine/community">
          Community
</a>      </span>

  </nav>
</div>

<div id="js-flash-container">

</div>




<div class="breadcrumb blob-breadcrumb">
  <label for="blob-history-checkbox" class="blob-history-label">
    <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"/></svg>
  </label>
  <span class="filetype-icon"><svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"/></svg></span>
  <strong class="final-path">corsarored.py</strong>
</div>


<input id="blob-history-checkbox"
       class="js-blob-history-checkbox blob-history-checkbox"
       type="checkbox"
       data-url="/dandag/qBittorrent_search_engine/latest_commit/master/corsarored.py">

<div class="blob-history">
  <a class="js-blob-history-link" href="/dandag/qBittorrent_search_engine/commits/master/corsarored.py">
    Loading latest commit…
</a></div>

<div class="bg-white">
    <div class="blob-file-content js-file-line-container">
      <div class="highlighted-blob tab-size" data-tab-size="8"><div class="code-body highlight"><pre><div class='line js-file-line' id='LC1'><span class="pl-c"><span class="pl-c">#</span> VERSION: 1.0</span></div><div class='line js-file-line' id='LC2'><span class="pl-c"><span class="pl-c">#</span> AUTHORS: shamalaya</span></div><div class='line js-file-line' id='LC3'><br></div><div class='line js-file-line' id='LC4'><span class="pl-k">from</span> helpers <span class="pl-k">import</span> download_file, retrieve_url</div><div class='line js-file-line' id='LC5'><span class="pl-k">from</span> novaprinter <span class="pl-k">import</span> prettyPrinter</div><div class='line js-file-line' id='LC6'><span class="pl-k">import</span> json</div><div class='line js-file-line' id='LC7'><span class="pl-k">from</span> urllib.parse <span class="pl-k">import</span> unquote</div><div class='line js-file-line' id='LC8'><span class="pl-k">import</span> cfscrape <span class="pl-c"><span class="pl-c">#</span>bypass cf cookie (need https://pypi.org/project/cfscrape and nodejs installed)</span></div><div class='line js-file-line' id='LC9'><br></div><div class='line js-file-line' id='LC10'><span class="pl-k">class</span> <span class="pl-en">corsarored</span>(<span class="pl-c1">object</span>):</div><div class='line js-file-line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>https://corsaro.red/<span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Corsaro.red<span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;supported_categories <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>movies<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>2<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>tv<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>music<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>3<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>games<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>6<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>anime<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>7<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>software<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>5<span class="pl-pds">&#39;</span></span>}</div><div class='line js-file-line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;searchurl <span class="pl-k">=</span> url <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>api/search<span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;limit <span class="pl-k">=</span> <span class="pl-c1">20</span> <span class="pl-c"><span class="pl-c">#</span> results per page</span></div><div class='line js-file-line' id='LC16'><br></div><div class='line js-file-line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">def</span> <span class="pl-en">search</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">what</span>, <span class="pl-smi">cat</span>):</div><div class='line js-file-line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scraper <span class="pl-k">=</span> cfscrape.create_scraper()</div><div class='line js-file-line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> page <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>,<span class="pl-c1">self</span>.limit):</div><div class='line js-file-line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>term<span class="pl-pds">&quot;</span></span>:unquote(what),<span class="pl-s"><span class="pl-pds">&quot;</span>category<span class="pl-pds">&quot;</span></span>: <span class="pl-c1">self</span>.supported_categories[cat],<span class="pl-s"><span class="pl-pds">&quot;</span>page<span class="pl-pds">&quot;</span></span>:page}</div><div class='line js-file-line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jsonresult <span class="pl-k">=</span> scraper.post(<span class="pl-c1">self</span>.searchurl,data).content.decode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>)</div><div class='line js-file-line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;json_object <span class="pl-k">=</span> json.loads(jsonresult)</div><div class='line js-file-line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nitems <span class="pl-k">=</span> <span class="pl-c1">len</span>(json_object[<span class="pl-s"><span class="pl-pds">&#39;</span>results<span class="pl-pds">&#39;</span></span>])</div><div class='line js-file-line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> nitems <span class="pl-k">==</span> <span class="pl-c1">0</span>:</div><div class='line js-file-line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">break</span></div><div class='line js-file-line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">else</span>:</div><div class='line js-file-line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">self</span>.processJson(json_object)</div><div class='line js-file-line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span> <span class="pl-c1">Exception</span> <span class="pl-k">as</span> e:</div><div class='line js-file-line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span>(e)</div><div class='line js-file-line' id='LC31'><br></div><div class='line js-file-line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">def</span> <span class="pl-en">getSingleData</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</div><div class='line js-file-line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>seeds<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>leech<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>size<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>link<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>desc_link<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>engine_url<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.url}</div><div class='line js-file-line' id='LC34'><br></div><div class='line js-file-line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">def</span> <span class="pl-en">processJson</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">json</span>):</div><div class='line js-file-line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData <span class="pl-k">=</span> <span class="pl-c1">self</span>.getSingleData()</div><div class='line js-file-line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> cur <span class="pl-k">in</span> json[<span class="pl-s"><span class="pl-pds">&#39;</span>results<span class="pl-pds">&#39;</span></span>]:</div><div class='line js-file-line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span> <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(cur[<span class="pl-s"><span class="pl-pds">&#39;</span>title<span class="pl-pds">&#39;</span></span>], cur[<span class="pl-s"><span class="pl-pds">&#39;</span>description<span class="pl-pds">&#39;</span></span>])</div><div class='line js-file-line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>desc_link<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> cur[<span class="pl-s"><span class="pl-pds">&#39;</span>link<span class="pl-pds">&#39;</span></span>]</div><div class='line js-file-line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>seeds<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> cur[<span class="pl-s"><span class="pl-pds">&#39;</span>seeders<span class="pl-pds">&#39;</span></span>]</div><div class='line js-file-line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>leech<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> cur[<span class="pl-s"><span class="pl-pds">&#39;</span>leechers<span class="pl-pds">&#39;</span></span>]</div><div class='line js-file-line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>size<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">str</span>(cur[<span class="pl-s"><span class="pl-pds">&#39;</span>size<span class="pl-pds">&#39;</span></span>])</div><div class='line js-file-line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;itemData[<span class="pl-s"><span class="pl-pds">&#39;</span>link<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> cur[<span class="pl-s"><span class="pl-pds">&#39;</span>magnet<span class="pl-pds">&#39;</span></span>]</div><div class='line js-file-line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prettyPrinter(itemData)</div><div class='line js-file-line' id='LC45'><br></div><div class='line js-file-line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">def</span> <span class="pl-en">download_torrent</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">info</span>):</div><div class='line js-file-line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span> Downloader <span class="pl-pds">&quot;&quot;&quot;</span></span></div><div class='line js-file-line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span>(download_file(info))</div><div class='line js-file-line' id='LC49'><br></div><div class='line js-file-line' id='LC50'><br></div><div class='line js-file-line' id='LC51'><span class="pl-c"><span class="pl-c">#</span> script test</span></div><div class='line js-file-line' id='LC52'><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</div><div class='line js-file-line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;cr <span class="pl-k">=</span> corsarored()</div><div class='line js-file-line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;cr.search(<span class="pl-s"><span class="pl-pds">&#39;</span>archlinux<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>all<span class="pl-pds">&#39;</span></span>)</div></pre></div></div>
    </div>
</div>


    <footer class="clearfix">
      <div class="container">
        <a href="#"><svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>

        <ul class="clearfix">
          <li>
            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-mobile-preference-form" action="/site/mobile_preference" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Qy5Hcu64aMI87sLRrdz9KGlOzBRQ1SdR7WFl3k9hmUxfzfPGvbX9YvS+c9ZYB8XEFUJvOOzisEXR/XJQgM81Jg==" />
              <input type="hidden" name="mobile" value="false">
              <input type="hidden" name="anchor" class="js-mobile-preference-anchor-field">

              <button type="submit" class="switch-to-desktop" data-ga-click="Mobile, switch to desktop, switch button">
                Desktop version
              </button>
</form>          </li>
          <li>
            <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out">
              Sign out
            </a>
          </li>
        </ul>
      </div>
    </footer>
  
    <script crossorigin="anonymous" async="async" integrity="sha512-ZurBZBu8gP3SdMfI/qBhJDL0QKg2AHBq4sE4wqB9iNUvltmDETStS3GDBbsEwJbgj9ewQHqrUSAQ4yw9i9CLBg==" type="application/javascript" src="https://github.githubassets.com/assets/mobile-bootstrap-95d486a2.js"></script>

  </body>
</html>
