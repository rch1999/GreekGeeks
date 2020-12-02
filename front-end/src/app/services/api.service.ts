import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../models/user.model';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    /* [FOR TESTING]: clears all users from the database */
    clearUsers() {
      throw new Error('Method not implemented.');
    }

    /* [FOR TESTING]: gets all users from the database */
    getUsers(): [User] {
      throw new Error('Method not implemented.');
    }

    getUserByEmail(email: string): User {
      throw new Error('Method not implemented.');
    }

    baseurl = "http://127.0.0.1:8000";
    httpHeaders = new HttpHeaders({'Content-type': 'application/json'});

    constructor(private http: HttpClient) {}
}