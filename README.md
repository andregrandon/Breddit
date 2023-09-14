# breddit-django

This is a an app, meant for testing skills of developer applying for work at Equaleyes. It's a clean Django application with only [DRF](https://www.django-rest-framework.org/) added to it.

## The task

Months ago, while eating breadsticks at our offices, we had a brilliant idea for a website. **breddit**. A website similar to [reddit](https://reddit.com), but also *completely* different. It's a way for bread lovers like ourselves to share their best bread recipes, vote on them, and discuss why garlic bread is the best.
We quickly started a plan on how to make this project work. A huge goal of ours was to use trending technologies, so we spent months researching which frameworks to use. We landed on Django, and even though our only backend developer had only heard of it, we decided this was enough experience.
After weeks of development, the backend was only about half way done. Then, out of nowhere, our backend guy's life completely changes - he starts a [keto diet](https://en.wikipedia.org/wiki/Ketogenic_diet)! This makes breddit against his religious beliefs, so he quits. We're left with a project half way done, but we already have our opening party planned!

That's where you come in. You're our only hope. Please, help us finish this project, and you'll be rewarded with a lifetime supply of breadsticks*.

The opening party is next week.

## Current state of the project

Currently, **breddit** has limited functionalities. You can see a list of posts and create posts. And that's pretty much it. Since this isn't a complete application login API is missing, but you can use Basic Authentication if needed. To keep it simple it's also using SQLite by default, but some data is provided within

## What needs to be added 

### Get a single post

Listing all posts is cool and all, but _sometimes_ we just want one, not all of them. Make an API that will return a single post by ID.

### Upvotes

If there are no upvotes, how will we know what is popular? You better add upovote/downvote API, so we can make sure our awesome posts dont't get lost.

### Post filters

We want to provide users with a few filters, which change how posts are ordered. Please add support for these filters:

* `fresh`: last added post should be on top
* `hot`: most upvoted post should be on top
* `trending`: most commented post should be on top

If you have any additional filters in mind, feel free to add them as well.

### Comments

Let's add comments to posts to express our opinion, otherwise what's the point? Add an endpoint where we can submit comments to posts. They should be editable, and deletable as well.

If you're feeling adventurous, you can add multi-level comments (comments that can be replied to).

### A few more things

If you still have time, there are a couple of other things you can do:

* Add a few tests, just to make sure everything works
* Export database with fixtures

That's it. If you have time, feel free to add any additional improvements as you see fit. If you have any questions, use Google.

## How to submit

Download this repository, and finish the task. Once you're done, create a zip archive, and email it to us.

If you have any questions, use Google. Unless it's about the API. In that case, feel free to contact us.

##### Disclaimer
\* The breadsticks are a lie. Sorry.
