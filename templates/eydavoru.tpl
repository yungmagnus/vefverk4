{% extends "base.html" %}

{% block title %}
    Vefverlsun - vöru eytt
{% endblock %}

{% block refresh %}
    <meta http-equiv="refresh"content="1; url={{url_for("karfa")}}">
{% endblock %}

{% block content %}
    <h1> Vöru úr körfu hefur verið eytt...
{% endblock %}