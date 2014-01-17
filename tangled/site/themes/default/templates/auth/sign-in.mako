<%inherit file="../base.mako"/>

<%block name="page_title">
  <h2>Sign In</h2>
</%block>

<%block name="content">
  <form method="post" action="${request.make_path('/sign-in')}">
    ${request.csrf_tag}

    <label for="username">Username or email address</label><br />
    <input type="text" name="username" /><br />

    <label for="password">Password</label><br />
    <input type="password" name="password" /><br />

    <% came_from = request.session.get('came_from') or request.referer %>
    <input type="hidden" name="came_from" value="${came_from}" />

    <input type="submit" value="Sign In" />
  </form>
</%block>
