---
layout: page
title: Random Thoughts
tagline: A wandering mind
---

<ul class="posts">
  {% for post in site.posts %}
    <article class="post">    
      
      <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
	  {{ post.date | date_to_string }}
      <div class="entry">
        {{ post.content | truncatewords:40}}
      </div>
      
      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
    </article>
  {% endfor %}
</ul>
