import { assertNotNull } from '@angular/compiler/src/output/output_ast';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ApiService } from '../services/api.service';
import { SignupComponent } from './signup.component';

describe('SignupComponent', () => {
  let component: SignupComponent;
  let backend: ApiService
  let fixture: ComponentFixture<SignupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SignupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SignupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    // clear all user info in the database between tests
    backend.clearUsers(); 
  });

  /* 
  RULES for the signup page (tests were based on this):
  1. You cannot sign up with an invalid email
  2. You cannot sign up with a password that does not satisfy:
    i. LESS THAN 6 characters OR
    ii. DOES NOT contain a symbol (!,?. ETC)
  3. your displayname must not already be taken by another user.
  4. Upon successful sign up, our backend will have 1 new user
  */

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // make sure each fundamental variable has a starting value of ""
  it('should start with empty fields', () => {
    expect(component.email).toEqual("");
    expect(component.displayName).toEqual("");
    expect(component.password).toEqual("");
  });

  // make sure we can't Sign Up with no info put in...
  it('should not allow sign up initially', () => {
    expect(component.email).toEqual("");
    expect(component.displayName).toEqual("");
    expect(component.password).toEqual("");
    try {
    component.signUp();
    } catch (error) {
      expect(error).toEqual(new Error("Please properly specify your credentials"))
    }
  });

  // make sure signing up works with a valid combination of user/pass
  it('should allow sign up on valid credentials', () => {
    let numusers: number = backend.getUsers().length;

    /* later this will be made far more secure */
    component.email = "zacharydward12@gmail.com";
    component.password = "admin1234!";
    component.displayName = "zacharydw"
    /* ^^^ this will be further encoded */

    try {
      component.signUp();
    } catch (error) {
      console.log(error); // this shouldn't happen...
    }
    // we should have 1 new user
    expect(backend.getUsers().length === numusers+1).toBeTruthy();
  });


  // make sure signing up doesn't work with a password less than 6 characters
  it('should prevent signup with a short password', () => {
    let numusers: number = backend.getUsers().length;

    component.email = "zacharydward12@gmail.com";
    component.password = "pass";
    component.displayName = "zacharydw";

    try {
      component.signUp();
    } catch(error) {
      expect(error).toEqual(new Error("Your password must be 6 characters or longer."));
    }
    expect(backend.getUsers().length === numusers).toBeTruthy(); // no users added to backend.

    /* change password to be longer than 6 characters but missing a symbol */
    component.password = "password";
    try {
      component.signUp();
    } catch(error) {
      expect(error).toEqual(new Error("Your password must have at least one symbol."));
    }
    expect(backend.getUsers().length === numusers).toBeTruthy(); // STILL no users added to backend.
  });

  // make sure signing up doesn't work with a taken displayName
  it('should prevent a user signing up with a taken display name', () => {
    /* get a username that is already in use */
    let usedName: string = backend.getUsers()[0].username;

    component.email = "zacharydward12@gmail.com";
    component.password = "admin1234!";
    component.displayName = usedName;

    try {
      component.signUp();
    } catch (error) {
      expect(error).toEqual(new Error("displayName is already in use."));
    }
  });
});
