.. fluent-ssml documentation master file, created by
   sphinx-quickstart on Fri Apr  7 09:22:23 2017.
   A
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to fluent-ssml's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Features
--------
 - Generate SSML markup using native Python code -- no text editor required
 - Because it's code, you can generate limitless markup variations (different volumes, rates, etc.)
 - Easy to follow code for developers and non-developers vs trying to read markup

Overview
--------
`fluent-ssml` uses a fluent coding style to "build" the SSML with a minimal
amount of code.

Quickstart Example
------------------

    from fluentssml import FluentSSML

    fs = FluentSSML()
    s = fs.rate_inc(50).txt("Sale, sale, sale.") \
          .rate_def().vol_x_loud().txt("Today!").break_m() \
          .txt("Call").rate_dec(30).say_as_phone().txt("202-555-1212") \
      .ssml
    print s

Installation
------------
Install $project by running:

    pip install fluent-ssml

Usage
-----
`fluent-ssml` is incredibly simple to use. You create a `FluentSSML` object and
then build your SSML using fluent-style syntax. At any time, you can get the
generated markup by calling `.ssml`



