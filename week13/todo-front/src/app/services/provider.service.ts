import { Injectable } from '@angular/core';
import {Task,TaskList} from '../models/models';
import {HttpClient} from '@angular/common/http';
import {MainService} from './main.service';
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists',{});
  }
  getTasks(id:number): Promise<Task[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks`,{});
  }
  deleteTask(id:number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`,{});
  }
  updateTask(id:number, newname:string): Promise<TaskList> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${id}/`,{
      name: newname
    });
  }
  createTask(newname:any): Promise<TaskList>{
    return this.post('http://127.0.0.1:8000/api/task_lists',{
      name: newname
    });
  }
  createTaskinTask(newname:any,status:any,id:number): Promise<Task>{
    return this.post(`http://127.0.0.1:8000/api/task_lists/${id}/tasks`,{
      name: newname,
      status: status,
      task_list: id
    })
  }
  deleteTaskinTask(id1:number,id2:number): Promise<Task>{
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id1}/tasks/${id2}`,{});
  }
  updateTaskinTask(newname:any,status:any,id:number,id2:number): Promise<Task>{
    return this.put(`http://127.0.0.1:8000/api/task_lists/${id}/tasks/${id2}`,{
      name: newname,
      status: status,
      task_list: id
    })
  }
}
