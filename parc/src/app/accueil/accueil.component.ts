import { Component, OnInit } from '@angular/core';
import { CritiqueService } from '../Service/critique.service';
import { AttractionService } from '../Service/attraction.service';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { AttractionInterface } from '../Interface/attraction.interface';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card'
import { MatDialog } from '@angular/material/dialog';
import { CritiqueDialogComponent } from '../critique-dialog/critique-dialog.component';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatTableModule],
  templateUrl: './accueil.component.html',
  styleUrls: ['./accueil.component.scss']
})
export class AccueilComponent 
{
  public displayedColumns: string[] = ['nom', 'description', 'difficulte', 'action'];
  public attractions: Observable<AttractionInterface[]> = this.attractionService.getAllAttraction();

  constructor(
    private attractionService: AttractionService,
    private critiqueService: CritiqueService,
    private dialog: MatDialog
  ) {}

  // Ouvrir le MatDialog pour ajouter une critique
  public openCritiqueDialog(attractionId: number): void {
    const dialogRef = this.dialog.open(CritiqueDialogComponent, {
      width: '400px',
      data: { attractionId }
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        // Logique pour actualiser la liste des critiques, si nécessaire
      }
    });
  }
}
