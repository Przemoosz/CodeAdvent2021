using System;
using System.IO;
using System.Collections.Generic;


/*
Creator: Przemysław Szewczak
Date: 27.12.2021
Source: https://adventofcode.com/2021/day/10
Language: C#
*/

namespace Solution
{
    internal class Challange1
    {
        public static void Main()
        {
            Polymers poly = new Polymers();
        }
        
    }
    public class Polymers
    {
        private string startingPolymer = "";
        private Dictionary<string, string> polymerPatterns = new Dictionary<string, string>();
        private Dictionary<string, long> polymerPairs = new Dictionary<string, long>();
        private Dictionary<char, long> letterCount = new Dictionary<char, long>();
        private char lastLetter = ' ';
         public Polymers()
        {
            Read();
            createFirstPairs();
            for (int i = 0; i < 40; i++)
            {
                createNewpairs();
            }
            countLetters();
            long day14Result = result();
            Console.WriteLine($"Day 14 Challenge 2 result is: {day14Result}");
        }
        private void Read()
        {
            // Load data from file method
            int lineCount = 0;
            foreach (string line in File.ReadLines(
                         @"C:\Przemek\Python\PythonAdventCalendar\AdventOfCode\test_input.txt"))
            {
                if (lineCount == 0)
                {
                    startingPolymer = line.Trim();
                    lineCount += 1;
                    continue;
                }
                else if (lineCount == 1)
                {
                    lineCount += 1;
                    continue;
                }

                string[] pattern = line.Trim().Split(" -> ");
                polymerPatterns.Add(pattern[0], pattern[1]);
            }

        }
        
        public void showPattern()
        {
            // Showing pattern list - Not used in final Program
            Console.WriteLine("Showing all Patterns");
            foreach( KeyValuePair<string, string> dict in polymerPatterns)
            {
                Console.WriteLine($"{dict.Key} -- {dict.Value}");
            }
        }
        
        public void showPairs()
        {
            // Showing actual pairs in polymers - Not used in final Program
            Console.WriteLine("Actual Pairs");
            foreach( KeyValuePair<string,long> kv in polymerPairs)
            {
                Console.WriteLine($"{kv.Key} = {kv.Value}");
            }
        }
        
        private void createFirstPairs()
        {
            // Creating first set of pairs after Read() method was called
            string pair = "";
            char[] polymerChars = startingPolymer.ToCharArray();
            for (int index = 0; index < startingPolymer.Length - 1; index++)
            {
                pair = polymerChars[index].ToString() + polymerChars[index + 1].ToString();
                if (polymerPairs.ContainsKey(pair))
                {
                    polymerPairs[pair] += 1;
                }
                else
                {
                    polymerPairs.Add(pair,1); 
                }
                
            }

            lastLetter = polymerChars[startingPolymer.Length - 1];
        }

        private void createNewpairs()
        {
            // Creates new pairs using actual pair dictionary
            var keys = polymerPairs.Keys;
            Dictionary<string, long> toAddition = new Dictionary<string, long>();
            foreach (string key in keys)
            {
                
                char[] polymerParts = key.ToCharArray();
                string firstPartPolymer = polymerParts[0].ToString() + polymerPatterns[key];
                string secondPartPolymer = polymerPatterns[key] + polymerParts[1].ToString();
                if (toAddition.ContainsKey(firstPartPolymer))
                {
                    toAddition[firstPartPolymer] += polymerPairs[key];
                }
                else
                {
                    toAddition.Add(firstPartPolymer,polymerPairs[key]);
                }
                //
                if (toAddition.ContainsKey(secondPartPolymer))
                {
                    toAddition[secondPartPolymer] += polymerPairs[key];
                }
                else
                {
                    toAddition.Add(secondPartPolymer,polymerPairs[key]);
                }
                //
                if (toAddition.ContainsKey(key))
                {
                    toAddition[key] -= polymerPairs[key];
                }
                else
                {
                    toAddition.Add(key,polymerPairs[key]*(-1));
                }


            }

            foreach (KeyValuePair<string, long> kv in toAddition)
            {
                if (polymerPairs.ContainsKey(kv.Key))
                {
                    polymerPairs[kv.Key] += kv.Value;
                }
                else
                {
                    polymerPairs.Add(kv.Key,kv.Value);
                }

                if (polymerPairs[kv.Key] == 0)
                {
                    polymerPairs.Remove(kv.Key);
                }
            }
        }
        
        private void addNewPair(string pair)
        {
            // Adding new pair to polymer pairs dictionary - Not used in final Program
            // Prototype method used before final solution
            string newPair = "";
            char[] polymerChars = pair.ToCharArray();
            // Console.WriteLine(polymerChars[0]);
            for (int index = 0; index < pair.Length - 1; index++)
            {
                newPair = polymerChars[index].ToString() + polymerChars[index + 1].ToString();
                // polymerPairs.ContainsKey(newPair)? polymerPairs[newPair]+=1 : polymerPairs.Add(pair,1);
                 if (polymerPairs.ContainsKey(newPair))
                 {
                     // Console.WriteLine($"Dict contains {newPair}");
                     polymerPairs[newPair] += 1;
                 }
                 else
                 {
                     // Console.WriteLine($"{newPair} does not exists");
                     polymerPairs.Add(newPair,1);
                 }
                // polymerPairs.Add(pair,1);
            }
        }

        private void countLetters()
        {
            // Counting first letters in pairs and adding last letter.
            foreach (KeyValuePair<string, long> kv in polymerPairs)
            {
                char[] letters = kv.Key.ToCharArray();
                if (letterCount.ContainsKey(letters[0]))
                {
                    letterCount[letters[0]] += kv.Value;
                }
                else
                {
                    letterCount.Add(letters[0],kv.Value);
                }
            }

            letterCount[lastLetter] += 1;
        }

        public void showLetters()
        {
            // Showing letters, used for visualisation - Not used in final program
            foreach (KeyValuePair<char, long> kv in letterCount)
            {
                Console.WriteLine($"{kv.Key}  =  {kv.Value}");
            }
        }

        private long result()
        {
            // Calculating result
            var values = letterCount.Values;
            long maxLetter = values.Max();
            long minLetter = values.Min();
            return maxLetter - minLetter;
        }
    }
}

