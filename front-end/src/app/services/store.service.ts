export class StoreService {
    loggedIn: boolean;
    // mock data for contacts
    contacts = ["Soloman Chau", "Jason Statham", "Sis Man",
    "Joe Biden", "The Real Sis Man"];
    numbers = ["911-911-9111", "123-764-1523", "196-397-4879", 
    "852-777-7777", "894-745-2222"];
    // mock data for activities
    activityHeaders = ["Soloman Chau wrote a note for Jason Statham",
    "Zach Ward assigned a task to Sis Man", "Joe Biden assigned a task\
    to The Real Sis Man"];
    activityText = ["Snapchat - jstatham01", 
    "Please complete alcohol.edu before you join",
    "Wear your mask and stay six feet apart! There is nothing\
    more important than maintaining your health."];
    activityType = ["contact", "task", "task"]

    constructor(){
        this.loggedIn = false;
    }

    logIn(){
        this.loggedIn = true;
    }

    logOut(){
        this.loggedIn = false;
    }

    getLoggedIn() {
        return this.loggedIn;
    }

    getContacts() {
        return this.contacts;
    }

    getNumbers() {
        return this.numbers;
    }

    getActivityHeaders() {
        return this.activityHeaders;
    }

    getActivityText() {
        return this.activityText;
    }

    getActivityType() {
        return this.activityType;
    }
}