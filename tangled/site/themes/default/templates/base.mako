<!DOCTYPE html>
<%namespace file="auth/sign-out-form.mako" import="sign_out_form" />
<html>
  <head>
    <title>${settings['site.title']}</title>
    % for name in ('normalize', 'base'):
      <% href = request.static_url('/static/stylesheets/{}.css'.format(name)) %>
      <link rel="stylesheet" type="text/css" href="${href}" />
    % endfor
  </head>
  <body>
    <div id="meta">
      % if not user:
        <a href="${request.make_path('/sign-up')}">Sign Up</a>
        &middot;
        <a href="${request.make_path('/sign-in')}">Sign In</a>
      % else:
        <a href="${request.make_path('/profile')}">My Profile</a>
        (${user.name or user.username or user.email})
        &middot;
        % if user.has_role('admin'):
          <a href="${request.make_path('/admin/users')}">Admin</a>
          &middot;
        % endif
        ${sign_out_form()}
      % endif
    </div>

    <div id="header">
      <%block name="header">
        <a href="/">
          <h1 id="title">${settings['site.title']}</h1>
          <h2 id="tagline">${settings['site.tagline']}&nbsp;</h2>
        </a>
      </%block>
    </div>

    <nav>
      <ul id="nav">
        <li><a href="/">Home</a></li>
        <li><a href="/entries">Entries</a></li>
        % for page in pages:
          <li><a href="">${page.title}</a></li>
        % endfor
      </ul>
    </nav>

    <h2 id="page-title">
      <%block name="page_title">Page Title Goes Here</%block>
    </h2>

    <%block name="flash">
      <% flash_messages = request.flash.pop() %>
      % if flash_messages:
        <ul id="flash">
          % for message in flash_messages:
            <li>${message}</li>
          % endfor
         </ul>
      % endif
    </%block>

    <div id="content">
      <%block name="content">
        Content goes here
      </%block>
    </div>

    <div id="footer">
      <%block name="footer">
        % if settings.get('site.copyright'):
          <div id="copyright">
            &copy; ${settings['site.copyright']}
          </div>
        % endif
        <div id="powered-by">
          Powered by <a href="http://tangledwebframework.org/">tangled.web</a>
        </div>
      </%block>
    </div>
  </body>
</html>
