import { Component, OnInit } from '@angular/core';
import { User } from '../models/user.model';
import { Task } from '../models/task.model';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-organization',
  templateUrl: './organization.component.html',
  styleUrls: ['./organization.component.scss']
})
export class OrganizationComponent implements OnInit {
  removeTask(task: Task) {
    throw new Error('Method not implemented.');
  }
  name: string; // each org. has a name
  admins: [User]; // each org. has a list of admins
  members: [User]; // each org. has a list of members
  tasks: [Task]; // each org. has a list of Tasks
  constructor(private backend: ApiService) { }

  ngOnInit(): void {
  }

  setName(orgname: string): void {

  }

  addTask(task: Task): void {

  }

  findTask(task: Task): boolean {
    return true;
  }

  getAdmins(): [User] {
    return this.admins;
  }

  getMembers(): [User] {
    return this.members;
  }

  getTasks(): [Task] {
    return this.tasks;
  }

  addMember(member: User) {
    this.members.push(member);
  }

  removeMember(member: User) {
    // remove member
  }

  reset () {
    // reset variables
  }


}
