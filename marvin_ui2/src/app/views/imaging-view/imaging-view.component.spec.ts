import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImagingViewComponent } from './imaging-view.component';

describe('ImagingViewComponent', () => {
  let component: ImagingViewComponent;
  let fixture: ComponentFixture<ImagingViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImagingViewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImagingViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
