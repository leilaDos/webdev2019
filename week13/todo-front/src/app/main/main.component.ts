import { Component, OnInit } from '@angular/core';
import {Task,TaskList} from '../models/models';
import {ProviderService} from '../services/provider.service';
import { now } from 'moment';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public task_lists: TaskList[] = [];
  public tasks: Task[] = [] ;
  public now = 0 ;
  public name: any = '';
  public taskname: any = '';
  public status: any = '';

  constructor( private  provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    });
  }
  getNewName(){
    let x = (<HTMLInputElement>document.getElementById('newName')).value;
    (<HTMLInputElement>document.getElementById('newName')).value = '';
    return x;
  }
  getStatus(){
    let x = (<HTMLInputElement>document.getElementById('status')).value;
    (<HTMLInputElement>document.getElementById('status')).value = '';
    return x;
  }
  getToDo(){
    let x = (<HTMLInputElement>document.getElementById('todo')).value;
    (<HTMLInputElement>document.getElementById('todo')).value = '';
    return x;
  }
  ChangeTask(TaskList: TaskList){
    this.now = TaskList.id;
    (<HTMLInputElement>document.getElementById('newName')).value = TaskList.name;
  }
  getTask() {
    this.provider.getTasks(this.now).then( res =>{
      this.tasks = res;
    });
  }

  deleteTaskList(){
    this.getNewName()
    this.provider.deleteTask(this.now).then(res=>{
      this.provider.getTaskLists().then(r =>{
        this.task_lists = r;
      })
    }
    )
    this.provider.getTasks(this.now).then(rr =>{
      this.tasks = rr;
    })
  }

  createTaskList(){
    this.name = this.getNewName();
    if(this.name!==''){
      this.provider.createTask(this.name).then(res =>{
        this.name = '';
        this.task_lists.push(res);
      })
    }
  }
  updateTaskList(){
    this.name = this.getNewName();
    if(this.name !== ''){
      this.provider.updateTask(this.now,this.name).then(res =>{
        this.name = '';
        this.provider.getTaskLists().then(r =>{
          this.task_lists = r;
        })
      })
    }
  }

  createTask(){
    this.taskname = this.getToDo();
    this.status = this.getStatus();
    // console.log(this.taskname+ " " + status+" "+now);
    this.provider.getTasks(this.now).then( res =>{
      this.provider.createTaskinTask(this.taskname,this.status,this.now).then(r =>{
        this.taskname = '';
        this.status = '';
        res.push(r);
        this.tasks = res;
      })
    })
  }
  deleleteTask(task: Task){
    this.provider.deleteTaskinTask(this.now,task.id).then(res =>{
      this.provider.getTasks(this.now).then(r =>{
        this.tasks = r;
      })
    })
  }
  updateTask(task: Task){ 
    if(task.name!=='' && task.status!==''){
      this.provider.updateTaskinTask(task.name,task.status,this.now,task.id).then(res =>{
        this.provider.getTasks(this.now).then(r =>{
          this.tasks = r;
        })
      })
    }
  }
}
