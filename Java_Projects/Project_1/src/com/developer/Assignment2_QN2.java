package com.developer;
import java.util.Random;//To generate random number
import java.util.Scanner;//To enable taking user input

public class Assignment2_QN2 {
    public static void main(String[] args) {
        Random rand = new Random(); // An instance of the random class
        int upperbound = 31;//Added 1 to include 30
        int random_number = rand.nextInt(upperbound);//Generate random number between 0 and 30


        //Asking the user to guess the number
        //Intro to the game
        System.out.println("Hello there. This is a guessing game. You are required to guess a number between 0 and 30." );
        System.out.println("Ready?! Here we go!");
        //Taking in user input
        Scanner sc = new Scanner(System.in);//reads from the standard input stream of the program.
        int counter = 0;//Count the number of times the user has guessed

        //Checking if the user's response is greater than or less than
        while (true) { //While true to make the program loop until user gets it right. Breaks at the else clause
            System.out.println("Enter you guess here: ");
            int user_num = sc.nextInt(); //reads the number entered
            counter =  counter + 1;//Adds one to the counter to record a guess trial
            if (user_num > random_number) {//checks if the user's input is greater than the random number
                System.out.println("Too high, try again");
            } else if (user_num < random_number) {//checks if user's input is less than the random number
                System.out.println("Too low, try again");
            }else{
                System.out.println("Matching.");//If the above two conditions not met, then it is a match
                System.out.println("Found after "+ counter + " trials.");//Prints out the number of trials
                break;//To break out of the loop
            }
        }

    }
}
