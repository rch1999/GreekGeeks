import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../models/user.model';
// import { AuthService } from '../services/auth/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {

  @Input() email: string;
  @Input() password: string;
  @Input() displayName: string;
  errorMsg: string;

  instructions: string = 'Please make sure that:\n (1) Your email is valid \n ' +
  '(2) Your password is at least 6 characters and \n (3) Your display name is at ' +
  'least 12 characters long';
  constructor(private router: Router) { }

    signUp() {
      const user: User = {
        email: this.email,
        password: this.password,
        username: this.displayName
      };

      // this is where we would register the user
    }

    handleError(errMessage: string): void {
      this.errorMsg = errMessage;
    }
}