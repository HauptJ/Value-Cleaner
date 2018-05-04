# Value-Cleaner

### Build Status
- **Linux:** [![Build Status](https://travis-ci.org/HauptJ/Value-Cleaner.svg?branch=master)](https://travis-ci.org/HauptJ/Value-Cleaner)
- **Windows:** [![Build status](https://ci.appveyor.com/api/projects/status/g5orvoxms31ujhee/branch/master?svg=true)](https://ci.appveyor.com/project/HauptJ/value-cleaner/branch/master)

Git pre and post commit hooks to remove values for private variables during commits. Before the files are commited, the pre-commit hook copies the original files to a temporary backup directory outside of the Git repository and then removes the values for specified variables. For example, the value of any variable that ends with **\_secret** will be replaced with **replace\_me** before it is commited. After the commit, the modified files will be restored using the files that were backed up.

Usage
------
Copy the **pre-commit**, **post-commit** hooks the **cmnds.py** and the **py-hook** files to the **git\_hooks** directory. Modify the **pre-commit** and **post-commit** hooks with your paramaters.


### Pre-Commit

Modify the command listed in pre-commit as follows:

```"pre" "source directory" "../backup directory" ".file extension" "_secret:.*" "_secret: replace_me"```

**Note 1:** The variables that you want to replace the values for should be tagged with an identifier such as __\_secret__. For example: __api_key_secret: API_key__ will be replaced with __api_key_secret: replace\_me__.

**Note 2:** Regular Expressions are used with to find the value to substitute / replace. For example if you use: __\_secret:.\*__ , the content of the line starting with __\_secret:__ will be replaced be replaced with __replace\_me__. If you use __\.\*__ regular expression, you may want to use something link this: ```"_secret:.*" "_secret: replace_me"```

[Regex Cheat Sheet](http://www.rexegg.com/regex-quickstart.html "Regex Cheat Sheet")

**Note 3:** If the text file does not have an extension, you should use **""** as the paramater.

**Note 4:** The backup directory must not be in the git repository and as a safeguard, the paramater must include __..__ at the beginning. For example: ```"../backup.dir```

### Post-Commit

Modify the command listed in post-commit as follows:

```"post" "source directory" "../backup directory"```
