from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Bryan",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Mountain hiking is an exhilarating experience. The thrill of reaching new heights, the panoramic views, and the crisp mountain air makes the journey worth every step.
        
        But it's not just about the summit. It's about the trail, the environment, and the memories you create along the way. Preparing for a mountain hike requires careful planning. From selecting the right gear to studying the trail map, every detail counts. 
        
        Respect for nature and understanding of the terrain are crucial to ensure safety. One of the best feelings in the world is standing on a mountain peak, looking out over the vast landscape, and knowing you conquered the climb.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Bryan",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
        Programming is a blend of art and science. It's about creating something out of nothing, using the power of logic and creativity. Whether it's building a website, a mobile app, or a complex algorithm, programming brings ideas to life      
        The world of programming is vast and diverse. From different languages to a multitude of tools, the learning never stops. Yet, the challenges faced are often rewarding. Debugging a piece of code can sometimes feel like solving a puzzle, and the satisfaction when everything runs smoothly is unparalleled     
        Embracing the coding journey means accepting failures, continuous learning, and celebrating small victories.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Bryan",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
        Nature has a way of calming the soul and recharging the mind. The serenity of a forest, the rhythm of waves crashing on a beach, or the simple joy of watching leaves fall, nature is a constant source of wonder.     
        Walking in the woods, one can't help but be in awe of the intricate details of the ecosystem. Every sound, from the chirping of birds to the rustle of leaves, tells a story. It's a world where everything is interconnected, and every creature, big or small, plays a part.     
        Taking a moment to connect with nature, to breathe in the fresh air, and to appreciate its beauty, is a reminder of the simple pleasures in life.
        """,
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
