import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { StoreService } from '../services/store.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  auth: boolean;
  constructor(private router: Router, private store: StoreService) {
    this.auth = this.store.getLoggedIn();
    console.log(this.auth);
   }

  ngOnInit(): void {
  }

  logout(): void {
    this.store.logOut();
    this.router.navigateByUrl('/login');
  }

}
