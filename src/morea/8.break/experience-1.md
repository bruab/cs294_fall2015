---
title: "Write code that breaks"
published: true
morea_id: break.experience1
morea_type: experience
morea_summary: "Fork/clone a repo full of errors, then make the errors your own"
morea_sort_order: 1
morea_labels:
 - 1-2 pts
 - 1-3 hours
 - closed
---

### Write Code That Breaks

On purpose, no less. This experience leads you in launching a pre-emptive strike against some of the Python errors that will eventually plague your code no matter how smart you are.

Fork the repository located at [https://github.com/cs294-python/errors](https://github.com/cs294-python/errors). Clone it and run `throw_err.py` a few times.

The script lets you choose from a list of error types, and then when it runs it crashes beautifully, throwing the exact error you chose. Amazing!

A peek at the code reveals that it's not so fancy underneath the hood. For each error option, the script simply uses the `raise` command to cause the error. We can do better.

#### For one point

Replace every line containing the `raise` command with a line or lines which cause the same error *without* using the command. The code you write should be an example of actual code that causes the error in question.

For example, where the script currently says

{% highlight python %}
elif error_type == "zerodivision":
    raise ZeroDivisionError
{% endhighlight %}

You should modify it to say something like

{% highlight python %}
elif error_type == "zerodivision":
    print(1/0)
{% endhighlight %}

#### For two points - Option A

Complete the above, and add four additional error types. (The readings can help you with this.) Write real code to cause errors -- don't use `raise`.

#### For two points - Option B

Complete the first part, and also implement your own error class. Add code which demonstrates the purpose of your error and raises it. Add a command line option to invoke it.
