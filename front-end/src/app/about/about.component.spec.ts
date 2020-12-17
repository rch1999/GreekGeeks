import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutComponent } from './about.component';

describe('AboutComponent', () => {
  let component: AboutComponent;
  let fixture: ComponentFixture<AboutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AboutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should toggle showcontributors upon function call', () => {
    /* before any toggles are made, by default the contributors to
    this codebase should not be displayed */
    expect(component.showContributors()).toBe(false);

     // show the contributors of our app via our component
    component.toggleContributors();

    // expect that our contributors are shown (boolean value is true)
    expect(component.showContributors()).toBe(true);
  });

  it('should toggle showing features upon function call', () => {
    /* before any toggles are made, by default the features of this app
     should not be displayed on the about page. */
    expect(component.showFeatures()).toBe(false);

    // show the features of our app via our component
    component.toggleFeatures();

    // expect that our features are now displayed
    expect(component.showFeatures()).toBe(true);
  });

  it('should show our techstack upon toggle switch', () => {
    /* before any toggles are made, by default the tech stack
    used to create this app should not be displayed */
    expect(component.showTech()).toBe(false);

    // show the tech stack of our app via our component
    component.toggleTechStack();

    // expect that our techstack is now displayed
    expect(component.showFeatures()).toBe(true);
  });

  it('should show the correct values of all our toggles', () => {
    /* before any switches are made, all variables should be false
    by default*/
    expect(component.showTech()).toBe(false);
    expect(component.showFeatures()).toBe(false);
    expect(component.showContributors()).toBe(false);

    expect(component.anyToggles()).toBe(false);
    /* after switching one of these toggles, we expect anyToggles
    to return true */

    component.toggleTechStack();

    expect(component.anyToggles()).toBe(true);

  });
});



