import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { Task } from '../models/task.model';
import { User } from '../models/user.model';
import { ApiService } from '../services/api.service';

import { OrganizationComponent } from './organization.component';

describe('OrganizationComponent', () => {
  let organization: OrganizationComponent;
  let backend: ApiService;
  let fixture: ComponentFixture<OrganizationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OrganizationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OrganizationComponent);
    organization = fixture.componentInstance;
    fixture.detectChanges();
    // reset organizations variables before each test
    organization.reset();
  });
 
  /* ORGANIZATION COMPONENT UNIT TESTS */

  // component should have no issues on creation
  it('should create', () => {
    expect(organization).toBeTruthy();
  });

  // setting the name should change the organizations name
  it('should allow setting of organization name', () => {
    organization.setName('betazeta');
    expect(organization.name).toEqual('betazeta');
  });

  // organization 'members' value should change if we add a non-null member
  it('should allow addition of non-null members', () => {
    let user: User = {uid: "001", username: "sonny"};
    // organization does not contain this new member...
    expect(organization.members.includes(user)).toBeFalse();
    organization.name = 'betazeta';
    organization.addMember(user);
    // now organization SHOULD contain this new member...
    expect(organization.members.includes(user)).toBeTrue();
  });

  // organization 'members' value shouldn't change if we add a null member
  it('should not allow addition of null members', () => {
    let user: User = null;
    organization.addMember(user);
    expect(organization.members.includes(user)).toBeFalse();
  });

  // organization members value should reflect removal of a valid member
  it('should allow removal of non-null members', () => {
    // set up our organization with our member
    let user: User = {uid: "001", username: "sonny"};
    organization.members = [user];

    expect(organization.members).toBe([user]);
    
    // remove the same member, expect an empty members list
    organization.removeMember(user);

    expect(organization.members).toBe([]);
  });

  // organization members should remain intact if removing a null value
  it('should not remove any members given a null value', () => {
    // set up our organization with our member
    let user: User = {uid: "001", username: "sonny"};
    organization.members = [user];

    expect(organization.members).toBe([user]);
    
    // remove null member, expect no change
    organization.removeMember(null);

    expect(organization.members).toBe([user]);
  });

  // add task should work for a valid, non-null task
  it('should allow addition of non-null tasks', () => {
    // define new task
    let task: Task = {tid: 223, desc: "St. Baldricks Philanthropy Event"};
    expect(organization.tasks.includes(task)).toBeFalse();
    
    // test adding our non-null task
    organization.addTask(task);

    // expect a change, we should see this task in our list of tasks
    expect(organization.tasks.includes(task)).toBeTrue();
  });

  // we do not want to react to null tasks
  it('should ignore addition of null tasks', () => {
    // define new task
    let task: Task = {tid: 223, desc: "St. Baldricks Philanthropy Event"};
    organization.tasks = [task];
    
    // test adding our non-null task
    organization.addTask(null);

    // expect a change, we should see this task in our list of tasks
    expect(organization.tasks).toBe([task]);
  });

  // orgs should be able to remove tasks that exist
  it('should allow removal of existent tasks', () => {
    // define new task
    let task: Task = {tid: 223, desc: "St. Baldricks Philanthropy Event"};
    organization.tasks = [task];
   

    // remove task, expect change
    organization.removeTask(task);
    expect(organization.tasks.includes(task)).toBeFalse();
  });

  // you can't remove a task that doesn't exist
  it('should ignore removal of non-existent tasks', () => {
    // define new task
    let task: Task = {tid: 223, desc: "St. Baldricks Philanthropy Event"};
    organization.tasks = [task];

    // remove task, expect nothing to change
    organization.removeTask({tid: 111, desc: "Catch some rest"});
    expect(organization.tasks).toBe([task]);
  });

  // you can't remove a null task
  it('should ignore removal of null tasks', () => {
    // define new task
    let task: Task = {tid: 223, desc: "St. Baldricks Philanthropy Event"};
    organization.tasks = [task];

    organization.removeTask(null);

    // expect no change
    expect(organization.tasks).toBe([task]);
  });
});
