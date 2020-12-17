import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-activity',
  templateUrl: './activity.component.html',
  styleUrls: ['./activity.component.scss']
})
export class ActivityComponent implements OnInit {
  @Input() header: string;
  @Input() text: string;
  @Input() type: string;
  constructor() { }

  ngOnInit(): void {
  }

}
