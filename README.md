# HclHackIITK
A cybersecurity hackathon
There are two types of programming questions, one is advanced coding and the other one is related to ML Classification.


You are required to write a Python function to read a file from the given 
. The file contains text lines and your function has to read each line and detect if the line is a palindrome along with count the number of characters.

If the line is a palindrome, then record the line number of this line in the file. The line number starts from 1. Not all lines are necessarily palindromes. Finally, count all the number of palindromes.
Your program needs to return a dictionary with the line number of a palindrome and number of characters in the palindrome (excluding blank spaces) along with a string representing the status of reading the file. 
If the file has no palindrome, the dictionary returned should contain 
If the URL is correct and the file is a txt file, the status message should be "file ok".
If the URL is correct but the file is not a txt file, the status message should be "file is not a text file".
If the URL is not a valid URL, the status message should be "the URL is incorrect".
Input Specification:
 The string value representing the URL of the file.
 Output Specification:
 Return an object of the "Result" class. The object should have:
 a dictionary with the key as the line number and value as the count of the number of characters
 a string representing the status message

 Example
  https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem1/defaulttestcase.txt

  Output:

   {2:4, 5:7, 6:30, 8:30, 9:9, 12:5, 14:11}
    "file ok"