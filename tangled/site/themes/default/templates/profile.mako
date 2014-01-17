<%inherit file="base.mako"/>

<%block name="page_title">Your Profile</%block>

<%block name="content">
  Name: ${user.name or 'Not set'}<br />
  Username: ${user.username or 'Not set'}<br />
  Email: ${user.email}<br />
</%block>
