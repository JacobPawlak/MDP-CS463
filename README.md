# MDP-CS463

## Markov Decision Processes
## Jacob Pawlak

### The state space:

s1	s2	s3	s4
s5	s6	s7	s8
s9	s10	s11	s12
s13	s14	s15	s16
 
### The reward function:

0	0	3	10
0	5	0	60
5	10	5	0
45	0	0	5

### The actions: up, down, left, right

### Probabilities:

0.7 to succeed
0.2 to go to the opposite direction
0.1 to stay
.96 discount

you bounce back, if you hit the wall (4 outside edges)


^Technical specs of the project.



### The final V^6:
325.262  505.62  992.144  1451.122  
654.076  906.254  1290.108  1493.123  
984.952  770.426  926.943  1289.41  
1143.319  980.726  727.452  933.736  

### the final directions are:
down  right  right  down  
down  right  right  right  
down  left  right  up  
down  left  left  up


### The final V*:

869.928  921.709  991.368  1065.816  
913.905  968.304  1034.044  1114.377  
893.493  924.45  973.44  1037.94  
933.405  889.77  922.418  986.651  

### the final directions are:
>  >  >  v  
>  >  >  >  
v  >  >  ^  
v  <  >  ^  



### What I learned from this assignment

I learned about planning and decision making, but I also learned
that people who play games (myself included), probably already do
this intuitively in their head. It's probably not as accurate as a
computer program, but at least they are getting a general sense of
when they imagine an MDP. I can probably only get about to a horizon
of two without scratch paper for a very simple game, but the intuition
has pretty much always been there. I actually learned some more about
Python and how indirect deep copying of a list works. I am surprised
I have never come accros that error before, but I was struggling to keep
my U` from being an exact (here meaning the eaxct same object pointer) copy
of U, because it was updating the Utility function after every cell was visited
which is not what I wanted it to do. SO I had to go find deepcopy, which I have
bookmarked to read more about later. I played around with the reward function a bit
after it was done - that was pretty neat because it would generate some zany 
direction policies.

### Favorite thing about CS463 from this semester

I really liked this course as a whole. The programs were bugger hard so
to be honest I probably will not recommend it to some of my friends looking
for an easy tech elective, because the class was not at all easy - but it 
was really cool to learn about the principles and algorithms I only had 
intuition on earlier. My favorite part though was probably learning about
Prolog. It's the first declarative programming language I have ever used, and 
I really liked the family tree application - I am thinking of writing a CGI
file for the Prolog code so that I can make a website for my family to update and
view our family tree. I dont know if it would work as well as I hope, but it sure
was fun to write the program! 









