# Python Developer Assessment

The aim of this Python assessment is to see how experienced a developer is, it is not a binary pass / fail test. It assess where a developer is on the Junior, Mid, Senior scale. It should be seen as a validation process and there are no right or wrong ways to solve the tasks defined.

There are four tasks to complete based around a list of dictionaries which represent pseudo-data for website URLs. Each task aims to test a developer's ability to manipulate and edit a list of data.

The data can be found in the `/websites/resouces/data.py` file.

The data can be viewed by running the following commands on the command line in Python's interactive mode:

```bash
python
>>> from websites.resources.data import WEBSITES
>>> print(WEBSITES)
```

The data structure is as follows, with five keys for each item:

```python
[
    {
        "name": "Google",
        "url": "https://www.google.co.uk",
        "domain": "google.co.uk",
        "secure": True,
        "value": 5
    },
    {
        "name": "Facebook",
        "url": "https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/",
        "domain": "facebook.com",
        "secure": True,
        "value": 4
    }
]
```
## Running the Program (Vincent's Assessment)

To run the code I wrote for this assessment, run `python3 main.py <task number>` where task number can be 1, 2, 3, or 4.


## Assessment Instructions

To complete the assessment please clone the repository.

```
git@github.com:RobDWaller/python-assessment.git
```

Write your code to complete the tasks and then store your code in a public git repository on GitHub or equivalent service. Alternatively zip the code up and submit via email.

You should not spend more than one hour completing this assessment. You will not be judged based on how many questions you answer but how well you answer each question.

### Note to Managers and Recruiters

This assessment should be used as part of an interview process. Developers who complete it deserve feedback on how they have performed and how they might improve. It should not be used as a filtering tool. 

## Tasks

### Task One: Find Data

Find and return a new list of data where each item's value key is equal to or greater than four.

**Example:** The below dictionary should be one of the items returned in the new list.

```python
{
    "name": "Facebook",
    "url": "https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/",
    "domain": "facebook.com",
    "secure": True,
    "value": 4
}
```

### Task Two: Amend Data

Amend the list so each domain key value is prepended with the string `www.`

**Example:** An amended dictionary should look as below where facebook.com has become www.facebook.com.

```python
{
    "name": "Facebook",
    "url": "https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/",
    "domain": "www.facebook.com",
    "secure": True,
    "value": 4
}
```

### Task Three: Cleanse Data

Some of the data is inaccurate, the secure key is set to False when the url key contains a URL beginning with `https://`. The opposite is also true in some cases.

The list should be cleansed and returned so the secure keys are accurate.

**Example:** The below dictionary should be amended to look as follows. It's current state is secure equals False even though the url key contains `https://`.

```python
{
    "name": "Bing",
    "url": "https://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A",
    "domain": "bing.com",
    "secure": True,
    "value": 3
}
```

### Task Four: Data Calculation

Add up all the value keys in the list and return an integer.

**Example:** If we added up the below value keys we'd get an integer of 9, 5 + 4.

```python
[
    {
        "name": "Google",
        "url": "https://www.google.co.uk",
        "domain": "google.co.uk",
        "secure": True,
        "value": 5
    },
    {
        "name": "Facebook",
        "url": "https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/",
        "domain": "facebook.com",
        "secure": True,
        "value": 4
    }
]
```

## Author

[@RobDWaller](https://twitter.com/RobDWaller)

If you have any questions feel free to message me on Twitter.
