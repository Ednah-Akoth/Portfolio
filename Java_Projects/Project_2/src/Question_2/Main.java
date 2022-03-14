package Question_2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
/*
* This program has 2 classes
*
* CAR class: Has one method to create cars
* TRAFFIC class: Has methods for each of the traffic lights
*       RED: Since no cars move here, this method has a for loop that has delays to make the red light last for 20 seconds
*       YELLOW: This method removes cars from the queue at  rate of 1 every 2 seconds and delays that make it last for 10 seconds
*       GREEN: This method removes cars at a rate of 1 every second. Has delay that makes it last for 30 sec
*
* MAIN PROGRAM STRUCTURE
* This program makes use of two threads.
*       1. Adds cars to an array. Once the car count reaches 100, no more cars are added
*       2. Has the traffic light simulator. Here, the  RED, YELLOW, & GREEN methods run
* Threads have been used to make the adding of cars and flow of traffic run simultaneously.
* Threads have also enabled having the adding of cars to occur independent of the traffic lights
*
* This program prints out the number of cars in the queue to help track how the car movements is occurring
* In the beginning, we will have both the adding cars thread and the traffic thread are running at the same time
* --> Cars are being added to the queue at intervals between 0 and 2 seconds. This is designed to simulate a heavily populated traffic intersection
* --> Immediately the program starts, the light is red. Thus, here, only addition of the cars to thread will occur thus the increase in the size of the queue
* --> When the yellow lights come on, the cars are both being added and removed. The rate at which the cars are being removed may be slower than the addition of cars
*     thus the number of cars in the queue may continue increasing. The number may stay constant in the event that the rate at which it is being added is the same as the rate
*     at which it is being removed (1 car per 2 sec).
* --> When the green light comes on, the same thing applies. The rate of addition of the cars may be greater than their removal causing the queue to increase. It may also decrease
*     when the rate of removing (1 per second) is greater than the rate of addition (eg may be 1 per 0.5 seconds since the adding time interval is between 0 - 2 seconds)
*     green light moves cars faster than the yellow light, there will be times when the number of cars in the queue will be the same twice (eg the number of cars may be printed as
*     77 twice). Since the cars are being added at random time intervals between 0 and 1 sec, there may be times when the car is added after 1 sec, which is the same rate
*     at which the green light is removing the car, thus making the number of cars constant
*--> After the number of cars in the queue(arrayList) reaches 100, no more cars will be added. After this point, the movements of the traffic lights will become more
*    evident.
* --> The program only stops when there are no more cars in the array*/


public class Main {
    //THE CAR CLASS
    public static class Car {
        int car_plate;
        String type;

        //Class Constructor
        Car (int car_plate, String type) {
            this.car_plate = car_plate;
            this.type = type;
        }

        //Class method to create car
        public static Object create_car(){
            //Getting the car type from a list
            List<String> givenList = Arrays.asList("SUV", "Sedan", "Sports Car", "Minivan","V8", "Station Wagon");
            Random rand0 = new Random();
            int randomIndex = rand0.nextInt(givenList.size());
            String random_type = givenList.get(randomIndex);

            //Generating a random plate for the car
            Random rand1 = new Random();
            int car_plt = rand1.nextInt(10000);

            //Creating a car object
            Car car1= new Car(car_plt,random_type);

            //Returning the car that has been created
            return car1;
        }
    }

    //THE TRAFFIC LIGHTS CLASS
    public static class Traffic {


        //RED LIGHT
        public static void red(ArrayList<Object>arr) throws InterruptedException {
            //No cars move
            //lasts 20 seconds
            for (int i = 0; i < 20; i++) {//
                Thread.sleep(1000);
                System.out.println("Red Light");//To show that it is the red light working
                System.out.println("Cars in queue: " + arr.size());//To show the size of the queue. After the initial addition of cars is done, the number of cars under red light
                //should remain constant
            }
        }

        //YELLOW LIGHT
        public static void yellow(ArrayList<Object>arr,ArrayList<Object>arr_out) throws InterruptedException {
            //lasts 10 seconds
            //Moves cars out of the array: 2/sec
            for (int i =0; i < 5; i++) {
                //TO REMOVE CARS
                //Checking if array is empty
                if (arr.size() != 0) {
                    int index = 0;//to remove the car at the beginning of the queue. Traffic runs under the principle of first come first out. So the cars at the beginning
                    //of the queue ought to be removed first

                    //Adding the index 0 element to the array arr_out that has cars that have gone past traffic
                    arr_out.add(arr.get(index));
                    arr.remove(index);//Removing the car at index 0 from the queue

                    System.out.println("Yellow Light Moving Cars");
                    System.out.println("Cars in queue: " + arr.size());//To show the size of the queue.

                } else {
                    System.exit(0);//Once the list is empty, exit the whole program
                }


                Thread.sleep(2000);//To make the green light last for 10 seconds

            }

        }

        //GREEN LIGHT
        public static void green(ArrayList<Object>arr,ArrayList<Object>arr_out) throws InterruptedException {
            //Lasts 30seconds
            //Moves cars out of the array: 1/sec
            for (int i = 0; i <30;i++) {

                //TO REMOVE CARS
                //Checking if array is empty
                if (arr.size() != 0) {
                    int index = 0;//to remove the car at the beginning of the queue

                    //Adding the index 0 element to the array arr_out that has cars that have gone past traffic
                    arr_out.add(arr.get(index));
                    arr.remove(index);

                    System.out.println("Green Light Moving Cars");
                    System.out.println("Cars in queue: " + arr.size());

                } else {
                    System.exit(0);//Once the list is empty, exit the whole program
                }


                Thread.sleep(1000);//To make the green light last for 30 seconds



            }

        }
    }




    public static void main(String[] args) throws InterruptedException {
        //Array of Existing cars at the traffic light
//
        Object[] arr = {Car.create_car()};
        ArrayList<Object> array_List = new ArrayList<Object>(Arrays.asList(arr));//Convert the arr to a list to enable easier adding
        System.out.println(array_List.size());

        //Array where cars that have gone through the traffic light are
        Object[] arr_out = {};
        ArrayList<Object> array_List1 = new ArrayList<Object>(Arrays.asList(arr_out));//Convert the arr to a list to enable adding


//THREAD TO ADD CARS
        Thread thread = new Thread(() -> {
            while (array_List.size() < 100) {//While the limit of 100 hasn't been reached. Remember the index starts at 0, so 0-99 is 100 cars
                array_List.add(Car.create_car());//Add a car to the arrayList
                Random rand1 = new Random();
                int time = rand1.nextInt(2000);//Picks random duration between 0 and 1000 millisecond to provide interval of car generation
                try {
                    Thread.sleep(time);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }

        });



        //THREAD FOR THE TRAFFIC LIGHTS
        Thread thread1 = new Thread(()->{
            while (array_List.size()>0) {
                try {
                    Traffic.red(array_List);//Runs the red light function which stops the traffic
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("\n");
                try {
                    Traffic.yellow(array_List,array_List1);//Runs yellow light: cars move 1 per 2 seconds
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("\n");
                try {
                    Traffic.green(array_List,array_List1);////Runs Green light: cars move 1 per second
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("\n");
            }

        });

        thread.start();//Starts the thread that adds cars separately
        thread1.start();//Starts the traffic lights thread









    }
}
