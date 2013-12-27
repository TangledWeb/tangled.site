<%inherit file="base.mako"/>

<%block name="page_title">
  <h2>Entry</h2>
</%block>

<%block name="content">
  <h3>${entry.title}</h3>
  <div>${entry.content}</div>
</%block>
