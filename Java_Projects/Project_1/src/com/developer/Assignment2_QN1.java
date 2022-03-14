package com.developer;

import java.util.Stack; //imports stack data structure
import java.util.Scanner;//Enables taking user input
public class Assignment2_QN1 {
    //This solution uses a stack to add on the numbers,then pop them
    static Stack<Integer> num_stack = new Stack<>();//Stack to store the digits of the number

    //function to push numbers into the stack
    static void pushing_digits(int num){
        while (num !=0) {//while the number is not zero
            //To get the number to be pushed, divide by 10 and
            //get the remainder.That is the digit on the far right
            int to_be_pushed = num%10;
            System.out.println(to_be_pushed);
            num_stack.push(to_be_pushed);
            //Divide the number by 10 to remove the number that has just been pushed
            num = num / 10;
        }
    }
    //Function to reverse the number. The pushing function will be called here
    //Int is the return type of the function
    static int reverse_number(int num) {//int because its return value is an integer
        pushing_digits(num);//adding the numbers of the user's input to the stack
        int reversed_number = 0;
        int place_value = 1;//this holds the place value of digits. Will be multiplied by 10 successively
        //then multiplied by the respective popped number
        while (!num_stack.isEmpty()) {//while the stack is not empty
            int popped = num_stack.pop();
            System.out.println(popped);
            reversed_number = reversed_number + (popped * place_value);//Adds the popped number multiplied by its place value.
            place_value = place_value * 10; //To move to the next place value
        }
        return reversed_number;
    }

    public static void main(String[] args) {
        //Taking in user input
        //void means that this method does not have a return value
        Scanner sc = new Scanner(System.in);//reads from the standard input stream of the program.
        System.out.println("Enter the number you want to reverse here: ");
        int user_num = sc.nextInt(); //reads the number entered
        System.out.println(reverse_number(user_num));

    }

}
