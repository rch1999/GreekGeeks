import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {
  private techStackToggled: boolean;
  private contributorsToggled: boolean;
  private featuresToggled: boolean;
  constructor() {
    this.techStackToggled = false;
    this.contributorsToggled = false;
    this.featuresToggled = false;
  }

  ngOnInit() {
  }

  anyToggles() {
    return this.techStackToggled || this.contributorsToggled || this.featuresToggled;
  }

  showTech() {
    return this.techStackToggled;
  }

  showContributors() {
    return this.contributorsToggled;
  }

  showFeatures() {
    return this.featuresToggled;
  }

  toggleTechStack() {
    this.techStackToggled = !this.techStackToggled;
  }

  toggleContributors() {
    this.contributorsToggled = !this.contributorsToggled;
  }

  toggleFeatures() {
    this.featuresToggled = !this.featuresToggled;
  }

}