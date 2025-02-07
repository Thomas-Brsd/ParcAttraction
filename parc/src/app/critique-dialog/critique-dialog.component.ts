import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CritiqueService } from '../Service/critique.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-critique-dialog',
  templateUrl: './critique-dialog.component.html',
  standalone: true,
  imports: [
    CommonModule, MatFormFieldModule, MatDialogModule, MatInputModule, ReactiveFormsModule
  ],
  styleUrls: ['./critique-dialog.component.scss']
})
export class CritiqueDialogComponent {
  public critiqueForm: FormGroup;

  constructor(
    private dialogRef: MatDialogRef<CritiqueDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { attractionId: number },
    private formBuilder: FormBuilder,
    private critiqueService: CritiqueService,
    private _snackBar: MatSnackBar
  ) {
    console.log(this.data.attractionId);  // Affiche l'attractionId dans la console pour vérifier qu'il est bien transmis
  
    // Initialisation du formulaire
    this.critiqueForm = this.formBuilder.group({
      attractionId: [this.data.attractionId, Validators.required],  // Utilisation de '' si attractionId est indéfini
      nom: ['', Validators.required],
      prenom: ['', Validators.required],
      texte: ['', Validators.required],
      note: [1, [Validators.required, Validators.min(1), Validators.max(5)]],
    });
  }

  // Soumettre la critique
  public onSubmit(): void {
    console.log(this.critiqueForm.value);
    if (this.critiqueForm.valid) {
      this.critiqueService.postCritique(this.critiqueForm.value).subscribe(result => {
        this._snackBar.open(result.message, 'Fermer', { duration: 2000 });
        this.dialogRef.close(true); // Fermer le dialog après soumission
      });
    }
  }

  // Annuler et fermer le dialog
  public onCancel(): void {
    this.dialogRef.close();
  }
}
