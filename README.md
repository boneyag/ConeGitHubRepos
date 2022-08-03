basically, these scripts are adaptions from here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/Popularity/GitHub_Phase1.py.

Config.json contains configurations, such as your GitHub token (can be generated in github settings), maximum amount of projects to retrieve, what query to use, etc.

Also, within GitHub_Phase1.py you will notice this query here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/master/scripts/Popularity/GitHub_Phase1.py#L46.

There, you can set min amount of stars.

Also, in my adaption, I set fork:false so that I don't grab forked repos.

Whatever the min amount of stars you set, make sure to update that number on this line too: https://github.com/ualberta-smr/LibraryMetricScripts/blob/d089e2179c5c73224aa8084c5d1c6f7cd6933edb/scripts/Popularity/GitHub_Phase1.py#L77 --> I am not quite sure why this line exists, but num of stars has to match whatever is on line L46 (edited) 

And finally, query is also set here: https://github.com/ualberta-smr/LibraryMetricScripts/blob/d089e2179c5c73224aa8084c5d1c6f7cd6933edb/scripts/Popularity/GitHub_Phase1.py#L111

It's a bit weird because query is set in different places