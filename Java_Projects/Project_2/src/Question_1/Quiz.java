package Question_1;

import java.util.Scanner;

public class Quiz {
//Method to print introduction message
    public static void welcome() {
        //introduction message
        System.out.println("\nHello User! Welcome to the General Knowledge Trivia!!\n" +
                "*********************************************************************************************************\n" +
                "--> Here, you will be presented with a general Knowledge question that has 5 multiple choice options\n" +
                "--> You will pick an asnwer by typing in the letter of the choice you think is right and hit enter.\n" +
                "--> We will display the time it took you to answer the question as well as whether your answer is right or wrong\n" +
                "--> After each question, we will ask you if you want to continue with the trivia.\n" +
                "--> If your response is yes, we will display the next question to you.\n" +
                "--> if your response is no, then the game ends.\n");

        System.out.print("Do you want to continue? (yes or no): ");
        int ans = general_consent();//Stores the return value from the general consent method
        //Checking what the return value is to determine the next steps for the program
        if (ans == 1) { //Code to proceed
            System.out.println("Let's start");
            game();
        } else if (ans == 0) {//Code to terminate
            System.out.println("Goodbye!");
            System.exit(0);
        }
    }
    public static int general_consent(){//This function will be used generally to ask uses for consent to proceed
        int return_value;

        //create an object of Scanner to accept user input
        while (true) {//While true to keep looping until the user gives a valid response
            Scanner input = new Scanner(System.in);
//            System.out.println("Do you want to continue? (yes or no): ");
            String consent = input.nextLine();
            //conversion to lowercase and removal of all whitespace to give uniformity in answer
            String consent1 = consent.toLowerCase().replaceAll(" ", "");

            if (consent1.equals("yes")) {//If yes, change return value to 1
                return_value = 1;
                break;
            } else if (consent1.equals("no")) {//If no change return value to 0
                return_value = 0;
                break;
//
            } else {
                System.out.println("Please enter a valid response: yes or no");
            }

        }
        return return_value;
    }

    public static void play_again() {//Method that will be used after the user has answered all the questions. Asks whether they want to play again
        System.out.println("Welldone! You have finished the trivia!");
        System.out.println("Would you like to play the game again?");
        int continue_permission = general_consent();//Uses the consent method to get a response
        if (continue_permission == 1) {//If 1, they said yes, so start the game again
            game();
        } else {//Else terminate program
            System.out.println("Thank you for playing the game!! Bye!");
            System.exit(0);
        }
    }



    public static void game() {
        //Create a multidimensional array to have the questions, multiple choices and answers.
        String[][] Qns_choices_ans = {
                {"QN1: What is Africa's newest country?\n", " A. Azania\n B. Wakanda\n C. South Sudan\n D. Western Sahara\n E. Azawad", "C"},
                {"QN2: What alias did Nelson Mandela use while pretending to be a caretaker at Liliesleaf farm in Johannesburg?\n", " A. David Motsamayi\n B. The Black Pimpernel\n C. Big Man\n D. Mark Radebe\n E. Rolihlahla Ntoko", "A"},
                {"QN3: In what city is the Chinese-built headquarters of the African Union?\n", " A. Lagos\n B. Addis Ababa\n C. Ouagadougou\n D. Mombasa\n E. Johannesburg", "B"},
                {"QN4: Where is Nollywood, the second biggest movie industry in the world in terms of number of films made?\n", " A. Namibia\n B. Nairobi\n C. Nelspruit\n D. Nigeria\n E. Niamey", "D"},
                {"QN5: Who or what is Liberia's capital Monrovia named after?\n", " A. Marilyn Monroe, film star\n B. James Monroe, the fifth president of the United States\n C. It's just a random name\n D. Monroe trees, indigenous to the region\n E. The pre-colonial Monroe kingdom", "B"},
                {"QN6: What is Ushahidi?\n", " A. An African philosophy promoting communal values\n B. A crowd-sourcing platform used to monitor violence in Kenya in 2008\n C. A popular walking trail in Mozambique\n D. The policy of deferring to elders\n E. Not a real word", "B"},
                {"QN7: Who was the first person convicted by the international criminal court?\n", " A. Congolese warlord Thomas Lubanga\n B. Kenya's President Uhuru Kenyatta\n C. The architect of apartheid Hendrik Verwoerd\n D. Former British prime minister Tony Blair\n E. Former Ugandan leader Idi Amin", "A"},
                {"QN8: What did Gambian president Yahya Jammeh announce in 2007?\n", " A. That he was dropping the article 'the' from his country's name\n B. That foreign ngos would be banned\n C. That he could cure Aids in just three days with a special potion of secret herbs\n D. He Never made any public appearance\n E.That homosexuals are welcome in his country", "C"},
                {"QN9: Who performed at Zimbabwe's independence day celebrations in 1980?\n", " A. Bob Marley\n B. Davido\n C. Tracy Chapman\n D. Paul Simon\n E. Bono", "A"},
                {"QN10: How many black presidents have there been in South Africa?\n", " A. One\n B. Two\n C. Three\n D. Four\n E. Five", "D"},
                {"QN11: It cost $30m, stands taller than the Statue of Liberty and is built to last until 3200AD. What is it?\n", " A. Donald Trump's new hotel in Zanzibar, Tanzania\n B. The African Renaissance monument in Dakar, Senegal\n C. Pinnacle Towers in Nairobi, Kenya\n D. The statue of former Chinese president Hu Jintao in Lilongwe, Malawi\n E. A new library planned for Timbuktu in Mali, with EU and US funding", "B"},
                {"QN12: Which former DJ came to power in a 2009 coup in Madagascar?\n", " A. Papa Wemba\n B. Fally Ipupa\n C. Wally Za\n D. Fela Kuti\n E. Andry Rajoelina", "E"},
                {"QN13: Who is Africa's longest serving leader?\n", " A. Jomo Kenyatta of Kenya\n B. The Black Panther\n C. Nelson Mandela of South Africa\n D. Robert Mugabe of Zimbabwe\n E. Teodoro Obiang of Equatorial Guinea", "E"},
                {"QN14: Which publication described Africa as 'the hopeless continent' in 2000 and 'the hopeful continent' in 2011?\n", " A. The Guardian\n B. The Standard\n C. The New York Times\n D. The Sun\n E. The Economist", "E"},
                {"QN15: Which one of the following statements is NOT true?\n", " A. There are 55 countries in the African Union\n B. There are 55 countries in Africa\n C. Somaliland is not a country\n D. Africa is not a country\n E. Africa is great", "A"}

        };


        System.out.println("Welcome to the game");
        System.out.println("**************************************************************************");
        int question_counter = 0;

        while (question_counter <= Qns_choices_ans.length) {//While i is less than or equal to the number of questions
            System.out.println(Qns_choices_ans[question_counter][0]);//prints out the question
            System.out.println(Qns_choices_ans[question_counter][1]);//prints out the multiple choices
            long startTime = System.currentTimeMillis();//Start measuring the time here
            Scanner input = new Scanner(System.in);
            System.out.print("Enter your answer here: ");//User's answer
            String user_answer = input.nextLine();
            long endTime = System.currentTimeMillis();//Stop measuring the time here
            long time_taken = (endTime - startTime)/1000; //Converting time from milliseconds to seconds
            //Convert to uppercase and remove whitespaces to match the way answers have been stored
            String user_answer_modified = user_answer.toUpperCase().replaceAll(" ", "");
            if (user_answer_modified.equals(Qns_choices_ans[question_counter][2])) {//checking if the answer is correct
                System.out.println("Correct!");
                System.out.println("You took " + time_taken + " Seconds to answer the question");//Prints out time taken
                System.out.println("Do you want to continue? (yes or no): ");
                int consent2 = general_consent();//calls consent method for user's input
                if (consent2 == 1) {
                    question_counter = question_counter + 1;//Increases the question counter so that we move to the next question incase user wants to continue
                } else if (consent2 == 0) {//if user said no
                    System.out.println("Thank you for playing. Goodbye :)");
                    System.exit(0);
                }

            } else {//If answer is wrong
                System.out.println("Wrong answer!");
                System.out.println("You took " + time_taken + " Seconds to answer the question");
                System.out.println("Do you want to continue? (yes or no): ");
                int consent2 = general_consent();//calls consent method for user's input
                if (consent2 == 1) {
                    question_counter = question_counter + 1;//Increases the question counter so that we move to the next question incase user wants to continue
                } else if (consent2 == 0) { //if consent is no, exit
                    System.out.println("Thank you for playing. Goodbye :)");
                    System.exit(0);
                }
            }
            if (question_counter == 15) {//Check whether we have reached the last question. If we have, we call the method that asks the user whether they want to play again
                play_again();
            }

        }
//        play_again();
    }

    public static void main(String[] args) {
        welcome();//Welcome is the method that starts the entire program
    }

}

