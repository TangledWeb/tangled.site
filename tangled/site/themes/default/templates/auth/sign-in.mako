<%inherit file="../base.mako"/>

<%block name="page_title">Sign In</%block>

<%block name="content">
  <form method="post" action="${request.make_path('/sign-in')}">
    ${request.csrf_tag}

    <label for="username">Username or email address</label><br />
    <input type="text" name="username" /><br />

    <label for="password">Password</label><br />
    <input type="password" name="password" /><br />

    ## If the came_from param is present, that indicates that the user
    ## was redirected here when attempting to access a protected page.
    ## Otherwise, the user clicked the "Sign In" link or accessed the
    ## /sign-in page directly.
    <% came_from = request.params.get('came_from') or request.referer or '' %>
    <input type="hidden" name="came_from" value="${came_from}" />

    <input type="submit" value="Sign In" />
  </form>
</%block>
