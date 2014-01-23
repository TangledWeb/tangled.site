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
        <a href="${request.make_path('/profile')}">
          My Profile
          (${user.name or user.username or user.email})
        </a>
        &middot;
        % if user.has_role('admin'):
          <a href="${request.resource_url('admin')}">Admin</a>
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
      <ul class="nav">
        % if user.has_role('admin'):
          <li><a href="${request.resource_url('admin')}">Admin</a></li>
        % endif
        <li><a href="/">Home</a></li>
        <li><a href="${settings['site.entries.path']}">${settings['site.entries.title']}</a></li>
        % for page in pages:
          % if page.slug != settings['site.home']:
            <li><a href="/${page.slug}">${page.title}</a></li>
          % endif
        % endfor
      </ul>
    </nav>

    <div id="content">
      <h2 id="page-title">
          <%block name="page_title">Page Title Goes Here</%block>
      </h2>

      <%block name="flash">
        <% flash_messages = request.flash.pop('error') %>
        % if flash_messages:
          <ul class="flash error">
            % for message in flash_messages:
              <li>${message}</li>
            % endfor
          </ul>
        % endif

        <% flash_messages = request.flash.pop() %>
        % if flash_messages:
          <ul class="flash info">
            % for message in flash_messages:
              <li>${message}</li>
            % endfor
          </ul>
        % endif
      </%block>

      <%block name="content">
        Content goes here
      </%block>
    </div>

    ${next.body()}

    <div id="footer">
      <%block name="footer">
        % if settings.get('site.copyright'):
          <div id="copyright">
            &copy; ${settings['site.copyright'] | n}
          </div>
        % endif
        <div id="powered-by">
          Powered by <a href="http://tangledwebframework.org/">tangled.web</a>
        </div>
      </%block>
    </div>

    <%block name="javascripts">
      <!-- JavaScript tags go here -->
    </%block>
  </body>
</html>
