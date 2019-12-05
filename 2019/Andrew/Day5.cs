﻿using System;
namespace AoC2019
{
    public class Day5
    {
        public Day5()
        {
        }

        public void Run()
        {
            IntcodeComputer((int[])Data.Clone(),1);
            IntcodeComputer(Data, 5);

        }

        public static int Fetch(int mode, int[] Input, int i)
        {
            return (mode % 10 == 1 ? Input[i] : Input[Input[i]]);
        }

        public static int IntcodeComputer(int[] Input, int op3)
        {

            for (int i = 0; i < Input.Length; i ++)
            {
                int mode = Input[i] / 100;
                switch (Input[i]%100)
                {
                    case 1://add
                        Input[Input[i + 3]] = Fetch(mode, Input, i + 1) + Fetch(mode/10, Input, i + 2);
                        i += 3;
                        break;
                    case 2://multiply
                        Input[Input[i + 3]] = Fetch(mode, Input, i + 1) * Fetch(mode / 10, Input, i + 2);
                        i += 3;
                        break;
                    case 3://input
                        Input[Input[i + 1]] = op3;//console in
                        i += 1;
                        break;
                    case 4://output
                        Console.WriteLine("Output:" + Fetch(mode, Input, i + 1));
                        i += 1;
                        break;
                    case 5://jump if true
                        i += 2;
                        if (Fetch(mode, Input, i - 1) != 0)
                        {
                            i = Fetch(mode / 10, Input, i) - 1;
                        }
                        break;
                    case 6://jump if false
                        i += 2;
                        if (Fetch(mode, Input, i - 1) == 0)
                        {
                            i = Fetch(mode / 10, Input, i) - 1;
                        }
                        break;
                    case 7://less than
                        Input[Input[i + 3]] = Fetch(mode, Input, i + 1) < Fetch(mode / 10, Input, i + 2) ? 1 : 0;
                        i += 3;
                        break;
                    case 8://equals
                        Input[Input[i + 3]] = Fetch(mode, Input, i + 1) == Fetch(mode / 10, Input, i + 2) ? 1 : 0;
                        i += 3;
                        break;
                    case 99://exit
                        return 0;

                }
            }
            return Input[0];
        }

        public static int[] TestData = {3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 };

        public static int[] Data = {3,225,1,225,6,6,1100,1,238,225,104,0,1102,17,65,225,102,21,95,224,1001,224,-1869,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,101,43,14,224,1001,224,-108,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,57,94,225,1101,57,67,225,1,217,66,224,101,-141,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,64,34,225,1101,89,59,225,1102,58,94,225,1002,125,27,224,101,-2106,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,78,65,225,1001,91,63,224,101,-127,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1102,7,19,224,1001,224,-133,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,2,61,100,224,101,-5358,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,19,55,224,101,-74,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,74,68,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,479,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,644,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,659,101,1,223,223,1107,226,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226};
    }
}
