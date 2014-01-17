<%inherit file="../base.mako"/>

<%block name="page_title">
  <h2>Sign Up</h2>
</%block>

<%block name="content">
  <form method="post" action="${request.make_path('/sign-up')}">
    ${request.csrf_tag}

    <label for="username">Username (optional)</label><br />
    <input type="text" name="username" /><br />

    <label for="email">Email</label><br />
    <input type="email" name="email" /><br />

    <label for="password">Password</label><br />
    <input type="password" name="password" /><br />

    <input type="submit" value="Sign Up" />
  </form>
</%block>
