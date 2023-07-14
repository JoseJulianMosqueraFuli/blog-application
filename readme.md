# Django Blog Application

This is a simple blog application built using the Django web framework. In this project, you will learn the basics of Django and how to create a blog with essential functionalities.

## Getting started

To run this application using Docker, make sure you have Docker installed on your machine. Follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:JoseJulianMosqueraFuli/blog-application.git
```

2. Navigate into the cloned directory:

```bash
cd blog-application/mysite
```

3. Build and run the Docker containers:

```bash
docker-compose up --build
```

4. The application should now be running. You can access it in your browser at `http://localhost:8000`.

## Features

- Data models and migrations: Design and manage the database structure for the blog application.
- Views, templates, and URLs: Create views to handle user requests, define templates for rendering HTML pages, and map URLs to views.
- Canonical and SEO-friendly URLs: Learn how to create canonical URLs for models and build search engine optimized URLs for blog posts.
- Object pagination: Implement pagination to display a limited number of posts per page and provide navigation to browse through posts.
- Class-based views: Utilize Django's class-based views to simplify the code structure and enhance code reusability.
- Django forms: Implement forms to enable users to recommend posts by email and comment on blog posts.
- Implementing canonical URLs for models and SEO-friendly URLs for blog posts.
- Adding object pagination for improved user experience and navigation.
- Utilizing class-based views to enhance code organization and reusability.
- Integrating Django forms to allow users to recommend posts by email and comment on posts.
- Integrating third-party applications
- Using django-taggit to implement a tagging system
- Building complex QuerySets to recommend similar posts
- Creating custom template tags and filters to show a list of the latest posts and most commented posts in the sidebar
- Creating a sitemap using the sitemap framework
- Building an RSS feed using the syndication framework
- Implementing a full-text search engine with Django and PostgreSQL

## Next Steps

Stay tuned for more updates and further improvements to the blog application!

## License

This project is licensed under the [MIT License](LICENSE).
