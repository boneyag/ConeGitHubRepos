basically, these scripts are adaptions from here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/Popularity/GitHub_Phase1.py.

Config.json contains configurations, such as your GitHub token (can be generated in github settings), maximum amount of projects to retrieve, what query to use, etc.

Also, within GitHub_Phase1.py you will notice this query here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/Popularity/GitHub_Phase1.py#L48.

There, you can set min amount of stars.

Also, in my adaption, I set fork:false and archived:false so that I don't grab forked and archived repos.

Whatever the min amount of stars you set, make sure to update that number on this line too: https://github.com/ualberta-smr/LibraryMetricScripts/blob/d089e2179c5c73224aa8084c5d1c6f7cd6933edb/scripts/Popularity/GitHub_Phase1.py#L94 --> I am not quite sure why this line exists, but num of stars has to match whatever is on line L48 (edited) 

And finally, query is also set here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/d089e2179c5c73224aa8084c5d1c6f7cd6933edb/scripts/Popularity/GitHub_Phase1.py#L128

It's a bit weird because query is set in different places
