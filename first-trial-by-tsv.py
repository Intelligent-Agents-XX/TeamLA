Last login: Fri Apr 24 19:02:24 on ttys000
tsanjevvishnu@Sanjus-MacBook-Pro ~ % cd Documents/GitHub/TeamLA
tsanjevvishnu@Sanjus-MacBook-Pro TeamLA % python3 running_project.py 
WElCOME...!!!

Please type your first song: payphone
Traceback (most recent call last):
  File "running_project.py", line 85, in <module>
    song1, song2 = knn(df, 2, recent_history)
  File "running_project.py", line 7, in knn
    avg += dataframe.loc[dataframe["Song Name"] == p, dim].values[0]
IndexError: index 0 is out of bounds for axis 0 with size 0
tsanjevvishnu@Sanjus-MacBook-Pro TeamLA % Payphone
zsh: command not found: Payphone
tsanjevvishnu@Sanjus-MacBook-Pro TeamLA % python3 running_project.py
WElCOME...!!!

Please type your first song: Baby

Currently playing: Baby
            Upcoming song:2U, What Do You Mean

Type command here: next

Currently playing: 2U
            Upcoming song:What Do You Mean, Steal My Girl

Type command here: next

Currently playing: What Do You Mean
            Upcoming song:Steal My Girl, Hips Don't Lie

Type command here: next 

Currently playing: Steal My Girl
            Upcoming song:Hips Don't Lie, Love Me Like You Do

Type command here: skip-next
running_project.py:50: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df[mood][song_num] -= 0.5

Currently playing: Love Me Like You Do
            Upcoming song:Baby, Shape Of You

Type command here: next

Currently playing: Baby
            Upcoming song:Shape Of You, 2U

Type command here: skip-next

Currently playing: 2U
            Upcoming song:What Do You Mean, I Like Me Better

Type command here: skip-next

Currently playing: I Like Me Better
            Upcoming song:Steal My Girl, Shape Of You

Type command here: skip-next

Currently playing: Shape Of You
            Upcoming song:What Do You Mean, Perfect

Type command here: next

Currently playing: What Do You Mean
            Upcoming song:Perfect, Baby

Type command here: skip-next

Currently playing: Baby
            Upcoming song:2U, Steal My Girl

Type command here: skip-next

Currently playing: Steal My Girl
            Upcoming song:Perfect, Love Me Like You Do

Type command here: skip-next

Currently playing: Love Me Like You Do
            Upcoming song:2U, Shape Of You

Type command here: skip-next

Currently playing: Shape Of You
            Upcoming song:What Do You Mean, Perfect

Type command here: skip-next

Currently playing: Perfect
            Upcoming song:Thinking Out Loud, I Like Me Better

Type command here: next

Currently playing: Thinking Out Loud
            Upcoming song:I Like Me Better, Baby

Type command here: skip-next 

Currently playing: Baby
            Upcoming song:2U, What Do You Mean

Type command here: exit
44.44444444444444
tsanjevvishnu@Sanjus-MacBook-Pro TeamLA % 
