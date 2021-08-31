import { TestBed } from '@angular/core/testing';

import { FarPiCameraServiceService } from './far-pi-camera-service.service';

describe('FarPiCameraServiceService', () => {
  let service: FarPiCameraServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FarPiCameraServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
