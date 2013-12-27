<%inherit file="base.mako"/>

<%block name="page_title">
  <h2>Your Profile</h2>
</%block>

<%block name="content">
  Name: ${user.name or 'Not set'}<br />
  Username: ${user.username or 'Not set'}<br />
  Email: ${user.email}<br />
</%block>
