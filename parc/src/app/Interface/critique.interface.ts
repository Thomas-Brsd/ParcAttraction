export interface CritiqueInterface {
  id?: number;
  attractionId: number;
  nom: string;
  prenom: string;
  anonyme: boolean;
  texte: string;
  note: number;
}
